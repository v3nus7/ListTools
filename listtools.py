#!/usr/bin/env python3
"""
ListTools v5.0 - Main Launcher
Launches the appropriate interface based on user choice
Author: Mr Sina
"""

import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_launcher():
    """Show launcher menu."""
    clear_screen()
    
    print("""
╔══════════════════════════════════════════════════════════╗
║              LISTTOOLS v5.0 - PROFESSIONAL               ║
╚══════════════════════════════════════════════════════════╝

    Developer: Mr Sina
    Website: www.SinaAbdi.com
    
    Select Interface:
    
    [1] Graphical Interface (GUI) - Recommended
    [2] Console Interface (CLI)
    [3] Exit
    
╚══════════════════════════════════════════════════════════╝
""")

def main():
    """Main launcher."""
    show_launcher()
    
    try:
        choice = input("Enter choice [1-3]: ").strip()
        
        if choice == '1':
            print("\n🚀 Launching GUI...")
            try:
                import list_tools_gui
                list_tools_gui.main()
            except ImportError:
                print("\n❌ Error: tkinter not found!")
                print("Install with: sudo apt-get install python3-tk")
                print("\nFalling back to console mode...")
                input("\nPress Enter to continue...")
                import list_tools_console
                list_tools_console.main()
            except Exception as e:
                print(f"\n❌ Error launching GUI: {e}")
                print("\nFalling back to console mode...")
                input("\nPress Enter to continue...")
                import list_tools_console
                list_tools_console.main()
        
        elif choice == '2':
            print("\n🚀 Launching Console...")
            import list_tools_console
            list_tools_console.main()
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            sys.exit(0)
        
        else:
            print("\n❌ Invalid choice!")
            input("\nPress Enter to try again...")
            main()
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
