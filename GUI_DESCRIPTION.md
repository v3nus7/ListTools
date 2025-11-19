# ListTools v5.0 - GUI Description

## GUI Overview

The ListTools GUI is a modern, professional interface built with tkinter. Here's what users will see:

## Main Window

```
╔════════════════════════════════════════════════════════════════════════╗
║                         LIST TOOLS v5.0                                ║
║      Professional List & Combo Processing Tool | www.SinaAbdi.com     ║
╚════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────┐
│ [Line Counter] [Line Splitter] [Remove Duplicates] [Save Duplicates]│
│ [Combo Cracker] [Password Encoder] [File Splitter] [About]          │
└──────────────────────────────────────────────────────────────────────┘

┌─ Selected Tab Content ─────────────────────────────────────────────┐
│                                                                      │
│  [Tab-specific controls and options appear here]                    │
│                                                                      │
│  [File selection buttons]                                           │
│  [Configuration options]                                            │
│  [Action button]                                                    │
│                                                                      │
│  ┌─ Result ─────────────────────────────────────────────────────┐  │
│  │                                                                │  │
│  │  Output and results displayed here                            │  │
│  │  (Scrollable text area)                                       │  │
│  │                                                                │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘

┌─ Progress ──────────────────────────────────────────────────────────┐
│ Status: Ready                                                        │
│ [████████████████████                    ] 60%                       │
└──────────────────────────────────────────────────────────────────────┘
```

## Tab Descriptions

### 1. Line Counter Tab
```
╔═ Line Counter ═══════════════════════════════════════════════════╗
║  Count lines in a file                                            ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File: [/path/to/file.txt        ] [Browse]                ║
║                                                                   ║
║                    [Count Lines]                                  ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Counting lines in: /path/to/file.txt                        │ ║
║  │                                                              │ ║
║  │ Total lines: 1,234,567                                       │ ║
║  │                                                              │ ║
║  │ Total Lines: 1,234,567                                       │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 2. Line Splitter Tab
```
╔═ Line Splitter ══════════════════════════════════════════════════╗
║  Split lines by separator                                         ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File: [/path/to/combo.txt       ] [Browse]                ║
║                                                                   ║
║  Separator: [:]     Split Mode: [0: Left (first part)    ▼]      ║
║                                                                   ║
║                    [Split Lines]                                  ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Splitting: /path/to/combo.txt                                │ ║
║  │ Separator: ':'                                               │ ║
║  │ Mode: 0                                                      │ ║
║  │                                                              │ ║
║  │ Finished: 10,000 lines processed, 0 errors                   │ ║
║  │                                                              │ ║
║  │ Output saved to: split_combo.txt                             │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 3. Remove Duplicates Tab
```
╔═ Remove Duplicates ══════════════════════════════════════════════╗
║  Remove duplicate lines                                           ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File: [/path/to/list.txt        ] [Browse]                ║
║                                                                   ║
║  ☑ Only save lines appearing less than: [2    ] times            ║
║                                                                   ║
║                 [Remove Duplicates]                               ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Removing duplicates from: /path/to/list.txt                  │ ║
║  │                                                              │ ║
║  │ Total: 100,000 | Duplicates: 25,000 | Saved: 75,000         │ ║
║  │                                                              │ ║
║  │ Output saved to: unique_list.txt                             │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 4. Save Duplicates Tab
```
╔═ Save Duplicates ════════════════════════════════════════════════╗
║  Save lines that appear multiple times                            ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File: [/path/to/passwords.txt   ] [Browse]                ║
║                                                                   ║
║  Minimum count: [1000 ] (save lines appearing >= this many times) ║
║                                                                   ║
║                   [Save Duplicates]                               ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Finding duplicates in: /path/to/passwords.txt                │ ║
║  │ Minimum count: 1000                                          │ ║
║  │                                                              │ ║
║  │ Total: 10,000,000 | Duplicates: 50 | Saved (>=1000): 12     │ ║
║  │                                                              │ ║
║  │ Output saved to: duplicates_passwords.txt                    │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 5. Combo Cracker Tab
```
╔═ Combo Cracker ══════════════════════════════════════════════════╗
║  Crack hashed combos with wordlist                                ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Wordlist:    [/path/to/wordlist.txt   ] [Browse]                ║
║  Combo File:  [/path/to/hashed.txt     ] [Browse]                ║
║                                                                   ║
║  Hash Type: [md5        ▼]     Separator: [:]                    ║
║                                                                   ║
║                   [Crack Combo]                                   ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Cracking combo: /path/to/hashed.txt                          │ ║
║  │ Using wordlist: /path/to/wordlist.txt                        │ ║
║  │ Hash type: md5                                               │ ║
║  │                                                              │ ║
║  │ Loaded 100,000 passwords                                     │ ║
║  │ Cracked: 5,432                                               │ ║
║  │ Finished: 5,432 cracked, 4,568 not found                     │ ║
║  │                                                              │ ║
║  │ Output saved to: cracked_hashed.txt                          │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 6. Password Encoder Tab
```
╔═ Password Encoder ═══════════════════════════════════════════════╗
║  Encode passwords in combo                                        ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File: [/path/to/combo.txt       ] [Browse]                ║
║                                                                   ║
║  Hash Type: [sha256     ▼]     Separator: [:]                    ║
║                                                                   ║
║  Encode Mode: [1: Encode password only           ▼]              ║
║                                                                   ║
║                  [Encode Passwords]                               ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Encoding: /path/to/combo.txt                                 │ ║
║  │ Hash type: sha256                                            │ ║
║  │ Mode: 1                                                      │ ║
║  │                                                              │ ║
║  │ Finished: 50,000 lines processed, 0 errors                   │ ║
║  │                                                              │ ║
║  │ Output saved to: encoded_combo.txt                           │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 7. File Splitter Tab
```
╔═ File Splitter ══════════════════════════════════════════════════╗
║  Split large file into smaller files                              ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Input File:  [/path/to/large.txt      ] [Browse]                ║
║  Output Dir:  [/path/to/output         ] [Browse]                ║
║                                                                   ║
║  Lines per file: [1000000  ]                                      ║
║                                                                   ║
║                    [Split File]                                   ║
║                                                                   ║
║  ┌─ Result ────────────────────────────────────────────────────┐ ║
║  │ Splitting: /path/to/large.txt                                │ ║
║  │ Lines per file: 1,000,000                                    │ ║
║  │ Output directory: /path/to/output                            │ ║
║  │                                                              │ ║
║  │ Creating part 0                                              │ ║
║  │ Creating part 1                                              │ ║
║  │ Creating part 2                                              │ ║
║  │                                                              │ ║
║  │ Finished: 2,500,000 lines split into 3 files                 │ ║
║  │                                                              │ ║
║  │ Output directory: /path/to/output                            │ ║
║  └──────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 8. About Tab
```
╔═ About ══════════════════════════════════════════════════════════╗
║                                                                   ║
║                        LIST TOOLS v5.0                            ║
║             Professional List & Combo Processing Tool             ║
║                                                                   ║
║  Developer: Mr Sina                                               ║
║  Website: www.SinaAbdi.com                                        ║
║                                                                   ║
║  Features:                                                        ║
║  • Line Counter - Count lines in large files                      ║
║  • Line Splitter - Split combo lists by separator                 ║
║  • Duplicate Remover - Remove duplicate lines efficiently         ║
║  • Duplicate Saver - Save lines appearing multiple times          ║
║  • Combo Cracker - Crack hashed combos with wordlist             ║
║  • Password Encoder - Hash passwords in combo files              ║
║  • File Splitter - Split large files into smaller parts          ║
║                                                                   ║
║  Capabilities:                                                    ║
║  ✓ Supports files with billions of lines                         ║
║  ✓ High-speed processing                                         ║
║  ✓ Non-blocking GUI operations                                   ║
║  ✓ Professional error handling                                   ║
║  ✓ Multiple hash algorithm support                               ║
║  ✓ Open source and free                                          ║
║                                                                   ║
║  This tool is designed for professional security researchers      ║
║  and data analysts who work with large datasets.                  ║
║                                                                   ║
║  Version History:                                                 ║
║  v5.0 - Complete rewrite with GUI, professional code structure    ║
║  v4.0 - Original console version                                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

## Features

### User Experience
- **Tab-based Navigation**: Easy switching between tools
- **File Browsers**: Native file/directory selection dialogs
- **Progress Indicators**: Real-time progress bars during operations
- **Scrollable Results**: All output areas are scrollable
- **Non-blocking**: Long operations run in background threads
- **Error Handling**: User-friendly error messages in dialog boxes
- **Tooltips**: (Can be added) Hover help for all controls

### Visual Design
- **Professional Layout**: Clean, organized interface
- **Consistent Styling**: All tabs follow same design pattern
- **Color Scheme**: Professional colors (can be themed)
- **Font**: Clear, readable fonts throughout
- **Spacing**: Proper padding and margins
- **Responsive**: Adapts to window resizing

### Accessibility
- **Keyboard Navigation**: Tab through controls
- **Keyboard Shortcuts**: (Can be added) Ctrl+O for Open, etc.
- **Clear Labels**: All controls clearly labeled
- **Logical Flow**: Top-to-bottom, left-to-right flow
- **Status Messages**: Always visible progress/status

## Technical Details

### Threading Model
```
Main Thread (GUI)
    ↓
    ├─> Worker Thread 1 (Processing)
    ├─> Worker Thread 2 (Processing)
    └─> Worker Thread N (Processing)
         ↓
         └─> Progress Callbacks → Main Thread (Update UI)
```

### Progress Updates
- Progress bar starts on button click
- Status updates every 100,000 lines
- Non-blocking UI during processing
- Cancel button (can be added)

### Window Management
- Minimum size: 900x700 pixels
- Resizable: Yes
- Centered on screen at launch
- Remembers size (can be added)

## Launch Instructions

```bash
# Launch GUI directly
python3 list_tools_gui.py

# Or use the launcher
python3 listtools.py
# Then select: [1] Graphical Interface (GUI) - Recommended
```

## Screenshots Note

This is a text-based description. When the GUI runs, users will see:
- Native OS window decorations (title bar, minimize/maximize/close)
- Native file dialogs (OS-specific)
- ttk widgets with native OS styling
- Professional, clean appearance

The actual appearance will match the user's operating system theme and style.
