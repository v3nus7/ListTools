#!/usr/bin/env python3
"""
ListTools Console Version
Professional command-line interface for list and combo processing
Author: Mr Sina (Refactored)
Version: 5.0
"""

import os
import sys
from list_tools_core import ListToolsCore, get_available_hash_algorithms

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Colors for terminal
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Banner
print(Color.RED + Color.BOLD + '''
www.SinaAbdi.com

  _      _____  _____ _______   _______ ____   ____  _       _____ 
 | |    |_   _|/ ____|__   __| |__   __/ __ \\ / __ \\| |     / ____|
 | |      | | | (___    | |       | | | |  | | |  | | |    | (___  
 | |      | |  \\___ \\   | |       | | | |  | | |  | | |     \\___ \\ 
 | |____ _| |_ ____) |  | |       | | | |__| | |__| | |____ ____) |
 |______|_____|_____/   |_|       |_|  \\____/ \\____/|______|_____/ 
                                                                    
Dev: Mr Sina
Version: 5.0 Professional Edition
''' + Color.RESET)

def progress_callback(message: str, current: int):
    """Progress callback for console output."""
    print(f"{Color.CYAN}[Progress] {message}{Color.RESET}")

def get_input(prompt: str, default: str = "") -> str:
    """Get user input with optional default value."""
    if default:
        result = input(f"{Color.YELLOW}{prompt} [{default}]: {Color.RESET}").strip()
        return result if result else default
    return input(f"{Color.YELLOW}{prompt}: {Color.RESET}").strip()

def get_int_input(prompt: str, default: int = None) -> int:
    """Get integer input from user."""
    while True:
        try:
            val = get_input(prompt, str(default) if default else "")
            return int(val)
        except ValueError:
            print(f"{Color.RED}Please enter a valid number{Color.RESET}")

def main_menu():
    """Display main menu and get user choice."""
    menu = f'''{Color.GREEN}
            Please Enter Mode:
            
    {Color.CYAN}[0]{Color.WHITE} Show Line Count
    {Color.CYAN}[1]{Color.WHITE} Line Splitter
    {Color.CYAN}[2]{Color.WHITE} Remove Duplicate Lines
    {Color.CYAN}[3]{Color.WHITE} Save Duplicates
    {Color.CYAN}[4]{Color.WHITE} Combo Crack Offline
    {Color.CYAN}[5]{Color.WHITE} Encode Password on Combo
    {Color.CYAN}[6]{Color.WHITE} File Splitter
    {Color.CYAN}[7]{Color.WHITE} Developer Info
    {Color.CYAN}[8]{Color.WHITE} Launch GUI Version
    {Color.CYAN}[9]{Color.WHITE} Exit
    {Color.RESET}'''
    
    print(menu)
    return get_int_input("Select option", 9)

def mode_line_counter(core: ListToolsCore):
    """Mode 0: Count lines in file."""
    print(f"\n{Color.BOLD}=== LINE COUNTER ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    print(f"\n{Color.CYAN}Counting lines...{Color.RESET}")
    count, message = core.count_lines(filename)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_line_splitter(core: ListToolsCore):
    """Mode 1: Split lines by separator."""
    print(f"\n{Color.BOLD}=== LINE SPLITTER ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    separator = get_input("Split by (e.g., : ; , . @)", ":")
    
    print(f"""
{Color.CYAN}Split Modes:{Color.RESET}
    [0] Left (first part)
    [1] Right (second part)
    [2] Right 2 (third part)
    [3] Right 3 (fourth part)
    [4] Parts 2,3,4
    [5] Parts 1,2
    [6] Parts 1,2,3
    """)
    
    mode = get_int_input("Select split mode", 0)
    output_file = f"split_{filename}"
    
    print(f"\n{Color.CYAN}Processing...{Color.RESET}")
    processed, errors, message = core.split_lines(filename, output_file, separator, mode)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output: {output_file}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_remove_duplicates(core: ListToolsCore):
    """Mode 2: Remove duplicate lines."""
    print(f"\n{Color.BOLD}=== REMOVE DUPLICATES ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    use_threshold = get_input("Filter by occurrence count? (y/n)", "n").lower() == 'y'
    min_count = None
    
    if use_threshold:
        min_count = get_int_input("Save only lines appearing less than X times", 2)
    
    output_file = f"unique_{filename}"
    
    print(f"\n{Color.CYAN}Processing...{Color.RESET}")
    total, duplicates, saved, message = core.remove_duplicates(filename, output_file, min_count)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output: {output_file}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_save_duplicates(core: ListToolsCore):
    """Mode 3: Save duplicate lines."""
    print(f"\n{Color.BOLD}=== SAVE DUPLICATES ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    min_count = get_int_input("Minimum count threshold (save lines appearing >= X times)", 2)
    output_file = f"duplicates_{filename}"
    
    print(f"\n{Color.CYAN}Processing...{Color.RESET}")
    total, duplicates, saved, message = core.save_duplicates(filename, output_file, min_count)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output: {output_file}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_combo_cracker(core: ListToolsCore):
    """Mode 4: Crack combo offline."""
    print(f"\n{Color.BOLD}=== COMBO CRACKER (OFFLINE) ==={Color.RESET}")
    
    wordlist = get_input("Enter wordlist file")
    if not os.path.exists(wordlist):
        print(f"{Color.RED}Error: Wordlist not found{Color.RESET}")
        return
    
    combo_file = get_input("Enter combo file (with hashes)")
    if not os.path.exists(combo_file):
        print(f"{Color.RED}Error: Combo file not found{Color.RESET}")
        return
    
    print(f"\n{Color.CYAN}Available hash types:{Color.RESET}")
    hash_types = get_available_hash_algorithms()
    common_types = ['md5', 'sha1', 'sha256', 'sha512']
    print(f"  Common: {', '.join([h for h in common_types if h in hash_types])}")
    
    hash_type = get_input("Hash type", "md5")
    separator = get_input("Separator character", ":")
    output_file = f"cracked_{combo_file}"
    
    print(f"\n{Color.CYAN}Cracking...{Color.RESET}")
    cracked, not_found, message = core.crack_combo_offline(
        wordlist, combo_file, output_file, hash_type, separator
    )
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output: {output_file}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_password_encoder(core: ListToolsCore):
    """Mode 5: Encode passwords in combo."""
    print(f"\n{Color.BOLD}=== PASSWORD ENCODER ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    print(f"""
{Color.CYAN}Encode Modes:{Color.RESET}
    [0] Encode entire line
    [1] Encode password only (user:hash)
    [2] Encode username/email only (hash:password)
    """)
    
    mode = get_int_input("Select encode mode", 1)
    
    print(f"\n{Color.CYAN}Available hash types:{Color.RESET}")
    hash_types = get_available_hash_algorithms()
    common_types = ['md5', 'sha1', 'sha256', 'sha512']
    print(f"  Common: {', '.join([h for h in common_types if h in hash_types])}")
    
    hash_type = get_input("Hash type", "md5")
    separator = get_input("Separator character", ":")
    output_file = f"encoded_{filename}"
    
    print(f"\n{Color.CYAN}Encoding...{Color.RESET}")
    processed, errors, message = core.encode_combo(filename, output_file, hash_type, mode, separator)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output: {output_file}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_file_splitter(core: ListToolsCore):
    """Mode 6: Split large file."""
    print(f"\n{Color.BOLD}=== FILE SPLITTER ==={Color.RESET}")
    filename = get_input("Enter file name")
    
    if not os.path.exists(filename):
        print(f"{Color.RED}Error: File not found{Color.RESET}")
        return
    
    lines_per_file = get_int_input("Lines per file", 100000)
    output_dir = get_input("Output directory", "split_output")
    
    print(f"\n{Color.CYAN}Splitting...{Color.RESET}")
    total, file_count, message = core.split_file(filename, output_dir, lines_per_file)
    print(f"\n{Color.GREEN}{message}{Color.RESET}")
    print(f"{Color.GREEN}Output directory: {output_dir}{Color.RESET}")
    input("\nPress Enter to continue...")

def mode_dev_info():
    """Mode 7: Developer information."""
    info = f"""
{Color.BOLD}{Color.CYAN}╔══════════════════════════════════════════════════════════╗
║              LISTTOOLS v5.0 - DEVELOPER INFO             ║
╚══════════════════════════════════════════════════════════╝{Color.RESET}

{Color.YELLOW}Developer:{Color.RESET} Mr Sina
{Color.YELLOW}Website:{Color.RESET} www.SinaAbdi.com
{Color.YELLOW}Version:{Color.RESET} 5.0 Professional Edition

{Color.BOLD}{Color.GREEN}Features:{Color.RESET}
  ✓ High-speed processing for billion-line files
  ✓ Professional code structure and error handling
  ✓ GUI and console interfaces
  ✓ Multi-threaded operations
  ✓ Memory efficient algorithms
  ✓ Multiple hash algorithm support
  ✓ Open source and free

{Color.BOLD}{Color.GREEN}Capabilities:{Color.RESET}
  • Line counting
  • Line splitting/extraction
  • Duplicate removal/detection
  • Offline combo cracking
  • Password hashing
  • File splitting

{Color.BOLD}{Color.GREEN}Version History:{Color.RESET}
  v5.0 - Complete refactor, GUI, professional code
  v4.0 - Original console version

{Color.BOLD}{Color.MAGENTA}For Security Research & Data Analysis{Color.RESET}

{Color.CYAN}Use responsibly and legally!{Color.RESET}
"""
    print(info)
    input("\nPress Enter to continue...")

def mode_launch_gui():
    """Mode 8: Launch GUI version."""
    print(f"\n{Color.BOLD}=== LAUNCHING GUI ==={Color.RESET}")
    print(f"{Color.CYAN}Starting graphical interface...{Color.RESET}")
    
    try:
        import list_tools_gui
        list_tools_gui.main()
    except ImportError as e:
        print(f"{Color.RED}Error: Could not import GUI module{Color.RESET}")
        print(f"{Color.YELLOW}Make sure tkinter is installed: sudo apt-get install python3-tk{Color.RESET}")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"{Color.RED}Error launching GUI: {str(e)}{Color.RESET}")
        input("\nPress Enter to continue...")

def main():
    """Main application loop."""
    core = ListToolsCore(progress_callback=progress_callback)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Color.RED + Color.BOLD + '''
  _      _____  _____ _______   _______ ____   ____  _       _____ 
 | |    |_   _|/ ____|__   __| |__   __/ __ \\ / __ \\| |     / ____|
 | |      | | | (___    | |       | | | |  | | |  | | |    | (___  
 | |      | |  \\___ \\   | |       | | | |  | | |  | | |     \\___ \\ 
 | |____ _| |_ ____) |  | |       | | | |__| | |__| | |____ ____) |
 |______|_____|_____/   |_|       |_|  \\____/ \\____/|______|_____/ 
                                                                    
''' + Color.RESET)
        
        mode = main_menu()
        
        if mode == 9:
            print(f"\n{Color.GREEN}Goodbye!{Color.RESET}")
            break
        
        try:
            if mode == 0:
                mode_line_counter(core)
            elif mode == 1:
                mode_line_splitter(core)
            elif mode == 2:
                mode_remove_duplicates(core)
            elif mode == 3:
                mode_save_duplicates(core)
            elif mode == 4:
                mode_combo_cracker(core)
            elif mode == 5:
                mode_password_encoder(core)
            elif mode == 6:
                mode_file_splitter(core)
            elif mode == 7:
                mode_dev_info()
            elif mode == 8:
                mode_launch_gui()
            else:
                print(f"{Color.RED}Invalid option{Color.RESET}")
                input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}Operation cancelled by user{Color.RESET}")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\n{Color.RED}Error: {str(e)}{Color.RESET}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
