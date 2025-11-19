# Installation Guide - ListTools v5.0

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/v3nus7/ListTools.git
cd ListTools
```

### 2. Install Dependencies (if needed)

#### Linux/Ubuntu
```bash
# Install tkinter for GUI support
sudo apt-get update
sudo apt-get install python3-tk
```

#### macOS
```bash
# Python usually includes tkinter on macOS
# If not, install Python from python.org or using Homebrew
brew install python-tk
```

#### Windows
```bash
# Python installer usually includes tkinter
# If not, reinstall Python and check "tcl/tk and IDLE" option
```

### 3. Run ListTools

#### Option A: Main Launcher (Recommended)
```bash
python3 listtools.py
```
This shows a menu to choose between GUI and Console modes.

#### Option B: Direct GUI Launch
```bash
python3 list_tools_gui.py
```

#### Option C: Direct Console Launch
```bash
python3 list_tools_console.py
```

#### Option D: Legacy Version
```bash
python3 file4.py
```

## Verification

Test the installation:
```bash
# Test core functionality
python3 test_core.py

# Test performance
python3 test_performance.py
```

## Troubleshooting

### Problem: "No module named 'tkinter'"
**Solution:** Install tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS
brew install python-tk
```

### Problem: "Permission denied"
**Solution:** Make scripts executable:
```bash
chmod +x *.py
```

### Problem: GUI won't start
**Solution:** 
1. Check if running in headless environment (no display)
2. Use console version instead: `python3 list_tools_console.py`
3. Verify DISPLAY environment variable is set (Linux)

### Problem: Slow performance
**Solution:**
1. Ensure you're using Python 3.7 or higher
2. Close other heavy applications
3. For very large files (>100M lines), increase system RAM or use file splitting

## System Requirements

- **Python**: 3.7 or higher
- **RAM**: 2GB minimum, 4GB+ recommended for large files
- **Storage**: Varies based on file sizes being processed
- **OS**: Linux, macOS, Windows (any OS with Python support)
- **Display**: Required for GUI mode only

## Optional: Create Desktop Shortcut

### Linux
Create `listtools.desktop`:
```ini
[Desktop Entry]
Version=5.0
Type=Application
Name=ListTools
Comment=Professional List & Combo Processing Tool
Exec=python3 /path/to/ListTools/listtools.py
Icon=utilities-terminal
Terminal=false
Categories=Utility;Development;
```

### Windows
Create a batch file `ListTools.bat`:
```batch
@echo off
cd /d "%~dp0"
python listtools.py
pause
```

### macOS
Create an app wrapper using Automator or run directly from terminal.

## Usage Examples

### Example 1: Count Lines
```bash
python3 listtools.py
# Select option 2 (Console)
# Select option 0 (Line Counter)
# Enter filename: myfile.txt
```

### Example 2: Remove Duplicates via GUI
```bash
python3 list_tools_gui.py
# Click "Remove Duplicates" tab
# Browse for input file
# Click "Remove Duplicates" button
```

### Example 3: Programmatic Use
```python
from list_tools_core import ListToolsCore

core = ListToolsCore()
total, dups, saved, msg = core.remove_duplicates(
    "input.txt",
    "output.txt"
)
print(msg)
```

## Next Steps

1. Read [README.md](README.md) for feature details
2. Check examples in test files
3. Try with sample data in `test_data/` directory
4. Report issues on GitHub

## Support

- **Website**: www.SinaAbdi.com
- **GitHub**: https://github.com/v3nus7/ListTools
- **Issues**: Create an issue on GitHub for bugs or feature requests

---

**Note**: This tool is for educational and legitimate security research purposes only.
