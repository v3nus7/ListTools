# Usage Examples - ListTools v5.0

## Table of Contents
1. [Getting Started](#getting-started)
2. [GUI Examples](#gui-examples)
3. [Console Examples](#console-examples)
4. [Python API Examples](#python-api-examples)
5. [Real-World Scenarios](#real-world-scenarios)

## Getting Started

### Quick Launch
```bash
# Launch main menu
python3 listtools.py

# Or directly launch GUI
python3 list_tools_gui.py

# Or directly launch console
python3 list_tools_console.py
```

## GUI Examples

### Example 1: Count Lines in a File

**Steps:**
1. Launch GUI: `python3 list_tools_gui.py`
2. Click on "Line Counter" tab
3. Click "Browse" button
4. Select your file (e.g., `passwords.txt`)
5. Click "Count Lines" button
6. View results in the result area

**Expected Output:**
```
Counting lines in: passwords.txt

Total lines: 1,234,567

Total Lines: 1,234,567
```

---

### Example 2: Split Combo List (Extract Emails)

**Scenario:** You have a combo list in format `email:password` and want to extract only emails.

**Steps:**
1. Go to "Line Splitter" tab
2. Browse and select combo file
3. Set Separator: `:`
4. Choose Split Mode: "0: Left (first part)"
5. Click "Split Lines"

**Input File (`combo.txt`):**
```
user1@email.com:password123
user2@email.com:test456
user3@email.com:secret789
```

**Output File (`split_combo.txt`):**
```
user1@email.com
user2@email.com
user3@email.com
```

---

### Example 3: Remove Duplicates

**Scenario:** Clean a password list by removing all duplicate entries.

**Steps:**
1. Go to "Remove Duplicates" tab
2. Browse and select file
3. Optionally check "Only save lines appearing less than" and set threshold
4. Click "Remove Duplicates"

**Input File:**
```
password123
test456
password123
secret789
test456
```

**Output File:**
```
password123
test456
secret789
```

---

### Example 4: Find Common Passwords

**Scenario:** From a huge password list, find passwords that appear 1000+ times.

**Steps:**
1. Go to "Save Duplicates" tab
2. Browse and select password list
3. Set "Minimum count" to 1000
4. Click "Save Duplicates"

**Use Case:** This creates a list of the most commonly used passwords!

---

### Example 5: Crack Hashed Combo

**Scenario:** You have a combo list with MD5 hashes and want to crack them.

**Steps:**
1. Go to "Combo Cracker" tab
2. Browse for wordlist file (your password dictionary)
3. Browse for combo file (with hashes)
4. Select Hash Type: "md5"
5. Set Separator: ":"
6. Click "Crack Combo"

**Combo File (`hashed_combo.txt`):**
```
user1@email.com:5f4dcc3b5aa765d61d8327deb882cf99
user2@email.com:098f6bcd4621d373cade4e832627b4f6
```

**Wordlist File:**
```
password
test
admin
123456
```

**Output (`cracked_hashed_combo.txt`):**
```
user1@email.com:password
user2@email.com:test
```

---

### Example 6: Hash Passwords in Combo

**Scenario:** Convert plaintext passwords to MD5 hashes.

**Steps:**
1. Go to "Password Encoder" tab
2. Browse for combo file
3. Select Hash Type: "md5"
4. Set Separator: ":"
5. Choose Mode: "1: Encode password only"
6. Click "Encode Passwords"

**Input:**
```
user1@email.com:password123
user2@email.com:test456
```

**Output:**
```
user1@email.com:482c811da5d5b4bc6d497ffa98491e38
user2@email.com:0cbc6611f5540bd0809a388dc95a615b
```

---

### Example 7: Split Large File

**Scenario:** Split a 10GB file into 100MB chunks.

**Steps:**
1. Go to "File Splitter" tab
2. Browse for large file
3. Set "Lines per file": 1000000 (adjust based on file size)
4. Browse/enter output directory
5. Click "Split File"

**Result:** Creates multiple files: `part0_yourfile.txt`, `part1_yourfile.txt`, etc.

---

## Console Examples

### Interactive Mode

```bash
python3 list_tools_console.py
```

Then follow the colorful menu prompts!

### Example Session:
```
[0] Show Line Count
[1] Line Splitter
[2] Remove Duplicate Lines
...

Select option: 0
Enter file name: myfile.txt

[Progress] Counting: 100,000 lines
[Progress] Counting: 200,000 lines
...
Total lines: 1,234,567
```

---

## Python API Examples

### Example 1: Basic Line Counting

```python
from list_tools_core import ListToolsCore

core = ListToolsCore()
count, message = core.count_lines("large_file.txt")
print(f"File has {count:,} lines")
```

---

### Example 2: Remove Duplicates with Progress

```python
from list_tools_core import ListToolsCore

def my_progress(message, current):
    print(f"[{current:,}] {message}")

core = ListToolsCore(progress_callback=my_progress)
total, dups, saved, msg = core.remove_duplicates(
    "input.txt",
    "output.txt"
)
print(f"Removed {dups:,} duplicates, saved {saved:,} unique lines")
```

---

### Example 3: Batch Processing

```python
from list_tools_core import ListToolsCore
from pathlib import Path

core = ListToolsCore()

# Process all text files in a directory
for file in Path("./data").glob("*.txt"):
    print(f"Processing {file.name}...")
    
    # Remove duplicates
    output = f"cleaned_{file.name}"
    total, dups, saved, msg = core.remove_duplicates(
        str(file),
        str(file.parent / output)
    )
    print(f"  {msg}")
```

---

### Example 4: Custom Pipeline

```python
from list_tools_core import ListToolsCore

def process_combo_list(input_file):
    """Complete combo processing pipeline."""
    core = ListToolsCore()
    
    # Step 1: Remove duplicates
    print("Step 1: Removing duplicates...")
    _, _, _, msg = core.remove_duplicates(
        input_file,
        "step1_unique.txt"
    )
    print(f"  {msg}")
    
    # Step 2: Extract passwords
    print("Step 2: Extracting passwords...")
    _, _, msg = core.split_lines(
        "step1_unique.txt",
        "step2_passwords.txt",
        ":",
        1  # Right part (password)
    )
    print(f"  {msg}")
    
    # Step 3: Hash passwords
    print("Step 3: Hashing passwords...")
    _, _, msg = core.encode_combo(
        "step1_unique.txt",
        "step3_hashed.txt",
        "sha256",
        1,  # Hash password only
        ":"
    )
    print(f"  {msg}")
    
    print("\nPipeline complete!")

# Run pipeline
process_combo_list("my_combo.txt")
```

---

## Real-World Scenarios

### Scenario 1: Security Audit

**Goal:** Analyze leaked credentials to identify weak passwords.

```python
from list_tools_core import ListToolsCore

core = ListToolsCore()

# Find most common passwords
print("Finding common passwords...")
total, dups, saved, msg = core.save_duplicates(
    "leaked_passwords.txt",
    "common_passwords.txt",
    100  # Used 100+ times
)

print(f"Found {saved:,} common passwords used 100+ times")
```

---

### Scenario 2: Data Cleaning

**Goal:** Clean and prepare data for analysis.

```python
from list_tools_core import ListToolsCore

def clean_dataset(input_file):
    core = ListToolsCore()
    
    # Remove duplicates
    print("Removing duplicates...")
    core.remove_duplicates(
        input_file,
        "cleaned_data.txt"
    )
    
    # Split into manageable chunks
    print("Splitting into chunks...")
    core.split_file(
        "cleaned_data.txt",
        "chunks/",
        100000  # 100k lines per file
    )
    
    print("Data cleaning complete!")

clean_dataset("raw_data.txt")
```

---

### Scenario 3: Password Research

**Goal:** Build a custom password list for penetration testing.

```bash
# 1. Combine multiple password lists
cat rockyou.txt common-passwords.txt > combined.txt

# 2. Remove duplicates
python3 -c "
from list_tools_core import ListToolsCore
core = ListToolsCore()
core.remove_duplicates('combined.txt', 'unique_passwords.txt')
"

# 3. Extract most common (for targeted attacks)
python3 -c "
from list_tools_core import ListToolsCore
core = ListToolsCore()
core.save_duplicates('combined.txt', 'top_passwords.txt', 1000)
"
```

---

### Scenario 4: Combo List Processing

**Complete workflow for combo list analysis:**

```python
from list_tools_core import ListToolsCore
from pathlib import Path

def process_combo_leak(combo_file):
    """Process leaked combo list."""
    core = ListToolsCore()
    base = Path(combo_file).stem
    
    # 1. Remove duplicates
    print("1. Removing duplicates...")
    unique_file = f"{base}_unique.txt"
    core.remove_duplicates(combo_file, unique_file)
    
    # 2. Extract emails
    print("2. Extracting emails...")
    emails_file = f"{base}_emails.txt"
    core.split_lines(unique_file, emails_file, ":", 0)
    
    # 3. Extract passwords
    print("3. Extracting passwords...")
    passwords_file = f"{base}_passwords.txt"
    core.split_lines(unique_file, passwords_file, ":", 1)
    
    # 4. Find common passwords
    print("4. Finding common passwords...")
    common_file = f"{base}_common_passwords.txt"
    core.save_duplicates(passwords_file, common_file, 10)
    
    print("\nProcessing complete!")
    print(f"  Unique combos: {unique_file}")
    print(f"  Emails: {emails_file}")
    print(f"  Passwords: {passwords_file}")
    print(f"  Common passwords (10+): {common_file}")

# Run processing
process_combo_leak("leaked_combo.txt")
```

---

## Performance Tips

### For Large Files (1GB+)
1. **Use file splitter first** if you have limited RAM
2. **Process chunks separately** for better progress tracking
3. **Close other applications** to free up memory

### For Maximum Speed
1. **Use SSD storage** for input/output files
2. **Increase progress_interval** in core (less frequent callbacks)
3. **Use console version** instead of GUI for batch processing

### For Very Large Files (100GB+)
```python
# Process in streaming fashion
core = ListToolsCore()
core.progress_interval = 1000000  # Report every 1M lines

# Split into manageable chunks first
core.split_file(
    "huge_file.txt",
    "chunks/",
    10000000  # 10M lines per chunk
)

# Then process each chunk
for chunk in Path("chunks/").glob("*.txt"):
    core.remove_duplicates(str(chunk), f"cleaned_{chunk.name}")
```

---

## Troubleshooting

### GUI Freezes
- **Cause:** Processing large file
- **Solution:** This shouldn't happen! The GUI uses threading. If it does freeze, report as a bug.

### Out of Memory
- **Cause:** File too large for available RAM
- **Solution:** Use file splitter to break into smaller pieces first.

### Slow Performance
- **Cause:** Disk I/O bottleneck or CPU limitations
- **Solution:** 
  - Use faster storage (SSD)
  - Process smaller chunks
  - Reduce progress callback frequency

---

## Support

Need help? Check:
1. [README.md](README.md) - Feature overview
2. [INSTALL.md](INSTALL.md) - Installation guide
3. GitHub Issues - Report bugs or request features

---

**Developer:** Mr Sina | **Website:** www.SinaAbdi.com | **Version:** 5.0
