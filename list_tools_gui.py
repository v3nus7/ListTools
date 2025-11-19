"""
ListTools GUI Application
Graphical interface for list and combo processing utilities
Author: Mr Sina (Refactored)
Version: 5.0
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
from pathlib import Path
from typing import Optional
import sys

from list_tools_core import ListToolsCore, get_available_hash_algorithms


class ListToolsGUI:
    """Main GUI application for ListTools."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("ListTools v5.0 - Professional List & Combo Tools")
        self.root.geometry("900x700")
        
        # Initialize core
        self.core = ListToolsCore(progress_callback=self.update_progress)
        
        # Operation tracking
        self.is_processing = False
        self.current_thread: Optional[threading.Thread] = None
        
        # Setup UI
        self.setup_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center the window on screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Setup the user interface."""
        # Header
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(
            header_frame,
            text="LIST TOOLS v5.0",
            font=("Arial", 20, "bold")
        )
        title_label.pack()
        
        subtitle_label = ttk.Label(
            header_frame,
            text="Professional List & Combo Processing Tool | www.SinaAbdi.com",
            font=("Arial", 10)
        )
        subtitle_label.pack()
        
        # Main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_line_counter_tab()
        self.create_line_splitter_tab()
        self.create_duplicate_remover_tab()
        self.create_duplicate_saver_tab()
        self.create_combo_cracker_tab()
        self.create_password_encoder_tab()
        self.create_file_splitter_tab()
        self.create_about_tab()
        
        # Progress section
        progress_frame = ttk.LabelFrame(self.root, text="Progress", padding="5")
        progress_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.progress_var = tk.StringVar(value="Ready")
        self.progress_label = ttk.Label(progress_frame, textvariable=self.progress_var)
        self.progress_label.pack(fill=tk.X)
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=5)
    
    def create_line_counter_tab(self):
        """Create line counter tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Line Counter")
        
        # Instructions
        ttk.Label(tab, text="Count lines in a file", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=10)
        
        self.lc_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.lc_input_file, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.lc_input_file)).pack(side=tk.LEFT)
        
        # Action button
        ttk.Button(tab, text="Count Lines", command=self.run_line_counter, style="Accent.TButton").pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.lc_result = scrolledtext.ScrolledText(result_frame, height=10, wrap=tk.WORD)
        self.lc_result.pack(fill=tk.BOTH, expand=True)
    
    def create_line_splitter_tab(self):
        """Create line splitter tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Line Splitter")
        
        ttk.Label(tab, text="Split lines by separator", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.ls_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.ls_input_file, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.ls_input_file)).pack(side=tk.LEFT)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Separator:").pack(side=tk.LEFT, padx=5)
        self.ls_separator = tk.StringVar(value=":")
        ttk.Entry(options_frame, textvariable=self.ls_separator, width=10).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(options_frame, text="Split Mode:").pack(side=tk.LEFT, padx=5)
        self.ls_mode = tk.IntVar(value=0)
        mode_combo = ttk.Combobox(options_frame, textvariable=self.ls_mode, width=30, state="readonly")
        mode_combo['values'] = [
            "0: Left (first part)",
            "1: Right (second part)",
            "2: Right 2 (third part)",
            "3: Right 3 (fourth part)",
            "4: Parts 2,3,4",
            "5: Parts 1,2",
            "6: Parts 1,2,3"
        ]
        mode_combo.current(0)
        mode_combo.pack(side=tk.LEFT, padx=5)
        mode_combo.bind('<<ComboboxSelected>>', lambda e: self.ls_mode.set(int(mode_combo.get().split(':')[0])))
        
        # Action button
        ttk.Button(tab, text="Split Lines", command=self.run_line_splitter).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.ls_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.ls_result.pack(fill=tk.BOTH, expand=True)
    
    def create_duplicate_remover_tab(self):
        """Create duplicate remover tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Remove Duplicates")
        
        ttk.Label(tab, text="Remove duplicate lines", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.dr_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.dr_input_file, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.dr_input_file)).pack(side=tk.LEFT)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        self.dr_use_threshold = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="Only save lines appearing less than:",
            variable=self.dr_use_threshold
        ).pack(side=tk.LEFT, padx=5)
        
        self.dr_threshold = tk.IntVar(value=2)
        threshold_spin = ttk.Spinbox(options_frame, from_=2, to=1000000, textvariable=self.dr_threshold, width=10)
        threshold_spin.pack(side=tk.LEFT, padx=5)
        ttk.Label(options_frame, text="times").pack(side=tk.LEFT)
        
        # Action button
        ttk.Button(tab, text="Remove Duplicates", command=self.run_duplicate_remover).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.dr_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.dr_result.pack(fill=tk.BOTH, expand=True)
    
    def create_duplicate_saver_tab(self):
        """Create duplicate saver tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Save Duplicates")
        
        ttk.Label(tab, text="Save lines that appear multiple times", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.ds_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.ds_input_file, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.ds_input_file)).pack(side=tk.LEFT)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Minimum count:").pack(side=tk.LEFT, padx=5)
        self.ds_min_count = tk.IntVar(value=2)
        ttk.Spinbox(options_frame, from_=2, to=1000000, textvariable=self.ds_min_count, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Label(options_frame, text="(save lines appearing >= this many times)").pack(side=tk.LEFT)
        
        # Action button
        ttk.Button(tab, text="Save Duplicates", command=self.run_duplicate_saver).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.ds_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.ds_result.pack(fill=tk.BOTH, expand=True)
    
    def create_combo_cracker_tab(self):
        """Create combo cracker tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Combo Cracker")
        
        ttk.Label(tab, text="Crack hashed combos with wordlist", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Files
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.cc_wordlist = tk.StringVar()
        ttk.Label(file_frame, text="Wordlist:").grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        ttk.Entry(file_frame, textvariable=self.cc_wordlist, width=40).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.cc_wordlist)).grid(row=0, column=2, padx=5, pady=2)
        
        self.cc_combo = tk.StringVar()
        ttk.Label(file_frame, text="Combo File:").grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        ttk.Entry(file_frame, textvariable=self.cc_combo, width=40).grid(row=1, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.cc_combo)).grid(row=1, column=2, padx=5, pady=2)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Hash Type:").pack(side=tk.LEFT, padx=5)
        self.cc_hash_type = tk.StringVar(value="md5")
        hash_combo = ttk.Combobox(options_frame, textvariable=self.cc_hash_type, width=15)
        hash_combo['values'] = get_available_hash_algorithms()
        hash_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(options_frame, text="Separator:").pack(side=tk.LEFT, padx=5)
        self.cc_separator = tk.StringVar(value=":")
        ttk.Entry(options_frame, textvariable=self.cc_separator, width=10).pack(side=tk.LEFT, padx=5)
        
        # Action button
        ttk.Button(tab, text="Crack Combo", command=self.run_combo_cracker).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.cc_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.cc_result.pack(fill=tk.BOTH, expand=True)
    
    def create_password_encoder_tab(self):
        """Create password encoder tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="Password Encoder")
        
        ttk.Label(tab, text="Encode passwords in combo", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.pe_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.pe_input_file, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.pe_input_file)).pack(side=tk.LEFT)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Hash Type:").pack(side=tk.LEFT, padx=5)
        self.pe_hash_type = tk.StringVar(value="md5")
        hash_combo = ttk.Combobox(options_frame, textvariable=self.pe_hash_type, width=15)
        hash_combo['values'] = get_available_hash_algorithms()
        hash_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(options_frame, text="Separator:").pack(side=tk.LEFT, padx=5)
        self.pe_separator = tk.StringVar(value=":")
        ttk.Entry(options_frame, textvariable=self.pe_separator, width=10).pack(side=tk.LEFT, padx=5)
        
        mode_frame = ttk.Frame(tab)
        mode_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(mode_frame, text="Encode Mode:").pack(side=tk.LEFT, padx=5)
        self.pe_mode = tk.IntVar(value=1)
        mode_combo = ttk.Combobox(mode_frame, textvariable=self.pe_mode, width=30, state="readonly")
        mode_combo['values'] = [
            "0: Encode entire line",
            "1: Encode password only",
            "2: Encode username/email only"
        ]
        mode_combo.current(1)
        mode_combo.pack(side=tk.LEFT, padx=5)
        mode_combo.bind('<<ComboboxSelected>>', lambda e: self.pe_mode.set(int(mode_combo.get().split(':')[0])))
        
        # Action button
        ttk.Button(tab, text="Encode Passwords", command=self.run_password_encoder).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.pe_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.pe_result.pack(fill=tk.BOTH, expand=True)
    
    def create_file_splitter_tab(self):
        """Create file splitter tab."""
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="File Splitter")
        
        ttk.Label(tab, text="Split large file into smaller files", font=("Arial", 12, "bold")).pack(pady=5)
        
        # File selection
        file_frame = ttk.Frame(tab)
        file_frame.pack(fill=tk.X, pady=5)
        
        self.fs_input_file = tk.StringVar()
        ttk.Label(file_frame, text="Input File:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(file_frame, textvariable=self.fs_input_file, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=lambda: self.browse_file(self.fs_input_file)).pack(side=tk.LEFT)
        
        # Output directory
        dir_frame = ttk.Frame(tab)
        dir_frame.pack(fill=tk.X, pady=5)
        
        self.fs_output_dir = tk.StringVar()
        ttk.Label(dir_frame, text="Output Dir:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(dir_frame, textvariable=self.fs_output_dir, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(dir_frame, text="Browse", command=self.browse_directory).pack(side=tk.LEFT)
        
        # Options
        options_frame = ttk.Frame(tab)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Lines per file:").pack(side=tk.LEFT, padx=5)
        self.fs_lines_per_file = tk.IntVar(value=100000)
        ttk.Spinbox(options_frame, from_=1000, to=100000000, textvariable=self.fs_lines_per_file, width=15).pack(side=tk.LEFT, padx=5)
        
        # Action button
        ttk.Button(tab, text="Split File", command=self.run_file_splitter).pack(pady=10)
        
        # Result
        result_frame = ttk.LabelFrame(tab, text="Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.fs_result = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.fs_result.pack(fill=tk.BOTH, expand=True)
    
    def create_about_tab(self):
        """Create about/info tab."""
        tab = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(tab, text="About")
        
        # Info text
        info_text = """
        LIST TOOLS v5.0
        Professional List & Combo Processing Tool
        
        Developer: Mr Sina
        Website: www.SinaAbdi.com
        
        Features:
        • Line Counter - Count lines in large files
        • Line Splitter - Split combo lists by separator
        • Duplicate Remover - Remove duplicate lines efficiently
        • Duplicate Saver - Save lines appearing multiple times
        • Combo Cracker - Crack hashed combos with wordlist
        • Password Encoder - Hash passwords in combo files
        • File Splitter - Split large files into smaller parts
        
        Capabilities:
        ✓ Supports files with billions of lines
        ✓ High-speed processing
        ✓ Non-blocking GUI operations
        ✓ Professional error handling
        ✓ Multiple hash algorithm support
        ✓ Open source and free
        
        This tool is designed for professional security researchers
        and data analysts who work with large datasets.
        
        Version History:
        v5.0 - Complete rewrite with GUI, professional code structure
        v4.0 - Original console version
        """
        
        text_widget = scrolledtext.ScrolledText(tab, wrap=tk.WORD, font=("Arial", 10))
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(1.0, info_text)
        text_widget.config(state=tk.DISABLED)
    
    def browse_file(self, var: tk.StringVar):
        """Browse for a file."""
        filename = filedialog.askopenfilename(
            title="Select File",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        if filename:
            var.set(filename)
    
    def browse_directory(self):
        """Browse for a directory."""
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.fs_output_dir.set(directory)
    
    def update_progress(self, message: str, current: int):
        """Update progress display (called from worker thread)."""
        self.root.after(0, self._update_progress_ui, message, current)
    
    def _update_progress_ui(self, message: str, current: int):
        """Update progress UI (runs in main thread)."""
        self.progress_var.set(message)
    
    def start_operation(self):
        """Mark operation as started."""
        self.is_processing = True
        self.progress_bar.start(10)
    
    def finish_operation(self):
        """Mark operation as finished."""
        self.is_processing = False
        self.progress_bar.stop()
    
    def run_in_thread(self, target_func):
        """Run a function in a separate thread."""
        if self.is_processing:
            messagebox.showwarning("Busy", "An operation is already in progress. Please wait.")
            return
        
        self.start_operation()
        thread = threading.Thread(target=target_func, daemon=True)
        self.current_thread = thread
        thread.start()
    
    def run_line_counter(self):
        """Run line counter operation."""
        def task():
            try:
                input_file = self.lc_input_file.get()
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                self.lc_result.delete(1.0, tk.END)
                self.lc_result.insert(tk.END, f"Counting lines in: {input_file}\n\n")
                
                count, message = self.core.count_lines(input_file)
                
                self.lc_result.insert(tk.END, f"\n{message}\n")
                self.lc_result.insert(tk.END, f"\nTotal Lines: {count:,}\n")
                
                messagebox.showinfo("Success", message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_line_splitter(self):
        """Run line splitter operation."""
        def task():
            try:
                input_file = self.ls_input_file.get()
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                separator = self.ls_separator.get()
                if not separator:
                    messagebox.showerror("Error", "Please enter a separator")
                    return
                
                mode = self.ls_mode.get()
                output_file = str(Path(input_file).parent / f"split_{Path(input_file).name}")
                
                self.ls_result.delete(1.0, tk.END)
                self.ls_result.insert(tk.END, f"Splitting: {input_file}\n")
                self.ls_result.insert(tk.END, f"Separator: '{separator}'\n")
                self.ls_result.insert(tk.END, f"Mode: {mode}\n\n")
                
                processed, errors, message = self.core.split_lines(
                    input_file, output_file, separator, mode
                )
                
                self.ls_result.insert(tk.END, f"\n{message}\n")
                self.ls_result.insert(tk.END, f"\nOutput saved to: {output_file}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_duplicate_remover(self):
        """Run duplicate remover operation."""
        def task():
            try:
                input_file = self.dr_input_file.get()
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                output_file = str(Path(input_file).parent / f"unique_{Path(input_file).name}")
                min_count = self.dr_threshold.get() if self.dr_use_threshold.get() else None
                
                self.dr_result.delete(1.0, tk.END)
                self.dr_result.insert(tk.END, f"Removing duplicates from: {input_file}\n\n")
                
                total, duplicates, saved, message = self.core.remove_duplicates(
                    input_file, output_file, min_count
                )
                
                self.dr_result.insert(tk.END, f"\n{message}\n")
                self.dr_result.insert(tk.END, f"\nOutput saved to: {output_file}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_duplicate_saver(self):
        """Run duplicate saver operation."""
        def task():
            try:
                input_file = self.ds_input_file.get()
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                min_count = self.ds_min_count.get()
                output_file = str(Path(input_file).parent / f"duplicates_{Path(input_file).name}")
                
                self.ds_result.delete(1.0, tk.END)
                self.ds_result.insert(tk.END, f"Finding duplicates in: {input_file}\n")
                self.ds_result.insert(tk.END, f"Minimum count: {min_count}\n\n")
                
                total, duplicates, saved, message = self.core.save_duplicates(
                    input_file, output_file, min_count
                )
                
                self.ds_result.insert(tk.END, f"\n{message}\n")
                self.ds_result.insert(tk.END, f"\nOutput saved to: {output_file}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_combo_cracker(self):
        """Run combo cracker operation."""
        def task():
            try:
                wordlist = self.cc_wordlist.get()
                combo = self.cc_combo.get()
                
                if not wordlist or not combo:
                    messagebox.showerror("Error", "Please select both wordlist and combo file")
                    return
                
                hash_type = self.cc_hash_type.get()
                separator = self.cc_separator.get()
                output_file = str(Path(combo).parent / f"cracked_{Path(combo).name}")
                
                self.cc_result.delete(1.0, tk.END)
                self.cc_result.insert(tk.END, f"Cracking combo: {combo}\n")
                self.cc_result.insert(tk.END, f"Using wordlist: {wordlist}\n")
                self.cc_result.insert(tk.END, f"Hash type: {hash_type}\n\n")
                
                cracked, not_found, message = self.core.crack_combo_offline(
                    wordlist, combo, output_file, hash_type, separator
                )
                
                self.cc_result.insert(tk.END, f"\n{message}\n")
                self.cc_result.insert(tk.END, f"\nOutput saved to: {output_file}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_password_encoder(self):
        """Run password encoder operation."""
        def task():
            try:
                input_file = self.pe_input_file.get()
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                hash_type = self.pe_hash_type.get()
                separator = self.pe_separator.get()
                mode = self.pe_mode.get()
                output_file = str(Path(input_file).parent / f"encoded_{Path(input_file).name}")
                
                self.pe_result.delete(1.0, tk.END)
                self.pe_result.insert(tk.END, f"Encoding: {input_file}\n")
                self.pe_result.insert(tk.END, f"Hash type: {hash_type}\n")
                self.pe_result.insert(tk.END, f"Mode: {mode}\n\n")
                
                processed, errors, message = self.core.encode_combo(
                    input_file, output_file, hash_type, mode, separator
                )
                
                self.pe_result.insert(tk.END, f"\n{message}\n")
                self.pe_result.insert(tk.END, f"\nOutput saved to: {output_file}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)
    
    def run_file_splitter(self):
        """Run file splitter operation."""
        def task():
            try:
                input_file = self.fs_input_file.get()
                output_dir = self.fs_output_dir.get()
                
                if not input_file:
                    messagebox.showerror("Error", "Please select an input file")
                    return
                
                if not output_dir:
                    output_dir = str(Path(input_file).parent / "split_output")
                    self.fs_output_dir.set(output_dir)
                
                lines_per_file = self.fs_lines_per_file.get()
                
                self.fs_result.delete(1.0, tk.END)
                self.fs_result.insert(tk.END, f"Splitting: {input_file}\n")
                self.fs_result.insert(tk.END, f"Lines per file: {lines_per_file:,}\n")
                self.fs_result.insert(tk.END, f"Output directory: {output_dir}\n\n")
                
                total, file_count, message = self.core.split_file(
                    input_file, output_dir, lines_per_file
                )
                
                self.fs_result.insert(tk.END, f"\n{message}\n")
                self.fs_result.insert(tk.END, f"\nOutput directory: {output_dir}\n")
                
                messagebox.showinfo("Success", f"{message}\n\nOutput: {output_dir}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.finish_operation()
        
        self.run_in_thread(task)


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = ListToolsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
