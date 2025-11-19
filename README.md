# ListTools v5.0 - Professional Edition

**Professional List & Combo Processing Tool with Graphical Interface**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)](LICENSE)

## 🎯 Overview

ListTools v5.0 is a completely refactored, professional-grade tool for processing large word lists and combo files. This version includes a modern graphical user interface (GUI) with full support for non-blocking operations, making it perfect for handling files with billions of lines.

**Website:** [www.SinaAbdi.com](http://www.SinaAbdi.com)  
**Developer:** Mr Sina  
**Version:** 5.0 (Professional GUI Edition)

## ✨ Key Features

### 🚀 Performance
- **High-Speed Processing**: Optimized algorithms for maximum performance
- **Memory Efficient**: Handles files with billions of lines
- **Non-Blocking UI**: Progress tracking without freezing
- **Multi-threaded**: Long operations run in background threads

### 🛠️ Tools Included

1. **Line Counter** - Count lines in large files with progress tracking
2. **Line Splitter** - Split combo lists by separator (email:password extraction)
3. **Duplicate Remover** - Remove duplicate lines efficiently
4. **Duplicate Saver** - Save lines appearing multiple times (e.g., common passwords)
5. **Combo Cracker (Offline)** - Crack hashed combos using wordlist
6. **Password Encoder** - Hash passwords in combo files (MD5, SHA1, SHA256, etc.)
7. **File Splitter** - Split large files into smaller parts
8. **About/Info** - Developer information and tool capabilities

### 🎨 User Interface
- **Modern GUI**: Built with tkinter for cross-platform compatibility
- **Tab-based Interface**: Easy navigation between tools
- **File Browser**: Built-in file and directory selection
- **Progress Indicators**: Real-time progress bars and status messages
- **Error Handling**: User-friendly error messages and validation

## 📦 Installation

### Requirements
- Python 3.7 or higher
- tkinter (usually included with Python, or install separately)

### Linux/Ubuntu
```bash
# Install tkinter if needed
sudo apt-get update
sudo apt-get install python3-tk

# Clone the repository
git clone https://github.com/v3nus7/ListTools.git
cd ListTools
```

### Windows
```bash
# Python usually includes tkinter on Windows
# Clone the repository
git clone https://github.com/v3nus7/ListTools.git
cd ListTools
```

## 🚀 Usage

### Graphical Interface (Recommended)
```bash
python3 list_tools_gui.py
```

### Command Line (Legacy)
```bash
python3 file4.py
```

### Python API (Programmatic Access)
```python
from list_tools_core import ListToolsCore

# Create core instance
core = ListToolsCore()

# Count lines
count, message = core.count_lines("myfile.txt")
print(f"Lines: {count}")

# Remove duplicates
total, dups, saved, msg = core.remove_duplicates(
    "input.txt", 
    "output.txt"
)
print(msg)
```

## 📖 Feature Details

### Line Counter
Count the total number of lines in a file, perfect for large files where standard tools might fail.

### Line Splitter
Split combo files (email:password format) by separator:
- Mode 0: Extract left part (email)
- Mode 1: Extract right part (password)
- Mode 2-6: Various combination extractions

### Duplicate Remover
Remove all duplicate lines from a file. Optionally filter by occurrence count.

### Duplicate Saver
Save only lines that appear multiple times. Perfect for finding common passwords:
- Set minimum count threshold
- Identify frequently used passwords
- Build custom password lists

### Combo Cracker (Offline)
Crack hashed combos using a wordlist:
- Support for multiple hash algorithms (MD5, SHA1, SHA256, SHA512, etc.)
- Custom separator support
- Efficient dictionary-based cracking

### Password Encoder
Hash passwords in combo files:
- Mode 0: Encode entire line
- Mode 1: Encode password only (user:hash)
- Mode 2: Encode username only (hash:password)

### File Splitter
Split large files into smaller chunks:
- Specify lines per file
- Custom output directory
- Maintains file integrity

## 🔧 Technical Details

### Architecture
```
ListTools/
├── list_tools_core.py      # Core processing logic
├── list_tools_gui.py       # GUI application
├── file4.py                # Legacy console version
└── README.md               # Documentation
```

### Code Quality
- ✅ Professional code structure
- ✅ Type hints for clarity
- ✅ Comprehensive error handling
- ✅ Progress callback system
- ✅ Thread-safe operations
- ✅ Modular design
- ✅ Fully documented

## 🎯 Use Cases

### Security Research
- Password analysis
- Combo list processing
- Hash cracking operations
- Dictionary management

### Data Processing
- Large file manipulation
- Duplicate detection
- Data cleaning
- File splitting/merging

## 📝 Persian Documentation / مستندات فارسی

این ابزار یک برنامه حرفه‌ای برای کار با لیست‌های بزرگ و کمبو لیست‌ها است.

### قابلیت‌ها:
- ✅ پشتیبانی از فایل‌های تا میلیاردها خط
- ✅ رابط گرافیکی مدرن و کاربرپسند
- ✅ سرعت بسیار بالا در پردازش
- ✅ عدم هنگ کردن رابط کاربری در عملیات طولانی
- ✅ شمارش تعداد خطوط
- ✅ جداسازی خطوط (استخراج ایمیل یا پسورد)
- ✅ حذف خطوط تکراری
- ✅ ذخیره خطوط تکراری (پیدا کردن پسوردهای پرکاربرد)
- ✅ کرک کمبو آفلاین با ورد لیست
- ✅ هش کردن پسوردها (MD5, SHA1, SHA256 و...)
- ✅ تقسیم فایل‌های بزرگ به قسمت‌های کوچکتر

### نحوه استفاده:
```bash
python3 list_tools_gui.py
```

## 🐛 Bug Reports

Found a bug? Please create an issue on GitHub or contact via website.

## 📜 License

Open Source - Free to use and modify

## 🙏 Acknowledgments

Special thanks to all security researchers and data analysts who provided feedback during development.

## 📞 Contact

- **Website**: [www.SinaAbdi.com](http://www.SinaAbdi.com)
- **Developer**: Mr Sina
- **Version**: 5.0 Professional Edition

---

**Note**: This tool is for educational and legitimate security research purposes only. Users are responsible for ensuring compliance with applicable laws and regulations.
