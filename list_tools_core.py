"""
ListTools Core Module
Professional implementation of list and combo processing utilities
Author: Mr Sina (Refactored)
Version: 5.0
"""

import hashlib
import os
from typing import Callable, Dict, List, Optional, Tuple
from pathlib import Path


class ListToolsCore:
    """Core functionality for list and combo processing operations."""
    
    def __init__(self, progress_callback: Optional[Callable[[str, int], None]] = None):
        """
        Initialize ListTools core.
        
        Args:
            progress_callback: Optional callback function for progress updates
                             Signature: callback(message: str, current: int)
        """
        self.progress_callback = progress_callback
        self.progress_interval = 100000  # Report progress every 100k lines
        
    def _report_progress(self, message: str, current: int) -> None:
        """Report progress if callback is set."""
        if self.progress_callback:
            self.progress_callback(message, current)
    
    def count_lines(self, input_file: str) -> Tuple[int, str]:
        """
        Count the number of lines in a file.
        
        Args:
            input_file: Path to input file
            
        Returns:
            Tuple of (line_count, status_message)
        """
        try:
            line_count = 0
            with open(input_file, 'r', encoding='latin1', errors='ignore') as f:
                for line in f:
                    line_count += 1
                    if line_count % self.progress_interval == 0:
                        self._report_progress(f"Counting: {line_count:,} lines", line_count)
            
            message = f"Total lines: {line_count:,}"
            self._report_progress(message, line_count)
            return line_count, message
        except FileNotFoundError:
            return 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, f"Error: {str(e)}"
    
    def split_lines(self, input_file: str, output_file: str, separator: str,
                   split_mode: int) -> Tuple[int, int, str]:
        """
        Split lines by a separator and extract specific parts.
        
        Args:
            input_file: Path to input file
            output_file: Path to output file
            separator: Character(s) to split by
            split_mode: Mode for splitting (0-6)
                0: left (first part)
                1: right (second part)
                2: right 2 (third part)
                3: right 3 (fourth part)
                4: right 4 (second:third:fourth parts)
                5: left 2 (first:second parts)
                6: left 3 (first:second:third parts)
                
        Returns:
            Tuple of (processed_lines, error_count, status_message)
        """
        try:
            processed_lines = 0
            error_count = 0
            
            with open(input_file, 'r', encoding='latin1', errors='ignore') as fi, \
                 open(output_file, 'w', encoding='utf-8', errors='ignore') as fo:
                
                for line in fi:
                    processed_lines += 1
                    line = line.rstrip('\n\r')
                    parts = line.split(separator)
                    
                    try:
                        if split_mode == 0:
                            fo.write(parts[0] + '\n')
                        elif split_mode == 1:
                            fo.write(parts[1] + '\n')
                        elif split_mode == 2:
                            fo.write(parts[2] + '\n')
                        elif split_mode == 3:
                            fo.write(parts[3] + '\n')
                        elif split_mode == 4:
                            fo.write(separator.join([parts[1], parts[2], parts[3]]) + '\n')
                        elif split_mode == 5:
                            fo.write(separator.join([parts[0], parts[1]]) + '\n')
                        elif split_mode == 6:
                            fo.write(separator.join([parts[0], parts[1], parts[2]]) + '\n')
                    except IndexError:
                        error_count += 1
                    
                    if processed_lines % self.progress_interval == 0:
                        self._report_progress(
                            f"Processed: {processed_lines:,} lines, Errors: {error_count}",
                            processed_lines
                        )
            
            message = f"Finished: {processed_lines:,} lines processed, {error_count} errors"
            self._report_progress(message, processed_lines)
            return processed_lines, error_count, message
        except FileNotFoundError:
            return 0, 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, 0, f"Error: {str(e)}"
    
    def remove_duplicates(self, input_file: str, output_file: str,
                         min_count: Optional[int] = None) -> Tuple[int, int, int, str]:
        """
        Remove duplicate lines from a file.
        
        Args:
            input_file: Path to input file
            output_file: Path to output file
            min_count: If specified, only save lines that appear less than min_count times
            
        Returns:
            Tuple of (total_lines, duplicate_count, saved_lines, status_message)
        """
        try:
            total_lines = 0
            line_counts: Dict[str, int] = {}
            
            # First pass: count occurrences
            with open(input_file, 'r', encoding='utf-8', errors='ignore') as fi:
                for line in fi:
                    total_lines += 1
                    line_stripped = line.strip()
                    line_counts[line_stripped] = line_counts.get(line_stripped, 0) + 1
                    
                    if total_lines % self.progress_interval == 0:
                        self._report_progress(
                            f"Counting: {total_lines:,} lines, {len(line_counts):,} unique",
                            total_lines
                        )
            
            duplicate_count = total_lines - len(line_counts)
            
            # Second pass: save unique lines (or filtered by count)
            saved_lines = 0
            with open(output_file, 'w', encoding='utf-8', errors='ignore') as fo:
                for line_text, count in line_counts.items():
                    if min_count is None or count < min_count:
                        fo.write(line_text + '\n')
                        saved_lines += 1
                        
                        if saved_lines % self.progress_interval == 0:
                            self._report_progress(
                                f"Saving: {saved_lines:,} lines",
                                saved_lines
                            )
            
            message = f"Total: {total_lines:,} | Duplicates: {duplicate_count:,} | Saved: {saved_lines:,}"
            self._report_progress(message, saved_lines)
            return total_lines, duplicate_count, saved_lines, message
        except FileNotFoundError:
            return 0, 0, 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, 0, 0, f"Error: {str(e)}"
    
    def save_duplicates(self, input_file: str, output_file: str,
                       min_count: int) -> Tuple[int, int, int, str]:
        """
        Save only lines that appear more than min_count times.
        
        Args:
            input_file: Path to input file
            output_file: Path to output file
            min_count: Minimum count threshold (lines appearing >= min_count will be saved)
            
        Returns:
            Tuple of (total_lines, duplicate_count, saved_lines, status_message)
        """
        try:
            total_lines = 0
            line_counts: Dict[str, int] = {}
            
            # Count occurrences
            with open(input_file, 'r', encoding='latin1', errors='ignore') as fi:
                for line in fi:
                    total_lines += 1
                    line_stripped = line.strip()
                    line_counts[line_stripped] = line_counts.get(line_stripped, 0) + 1
                    
                    if total_lines % self.progress_interval == 0:
                        self._report_progress(
                            f"Counting: {total_lines:,} lines",
                            total_lines
                        )
            
            duplicate_count = sum(1 for count in line_counts.values() if count > 1)
            
            # Save lines that meet the threshold
            saved_lines = 0
            with open(output_file, 'w', encoding='utf-8', errors='ignore') as fo:
                for line_text, count in line_counts.items():
                    if count >= min_count:
                        fo.write(line_text + '\n')
                        saved_lines += 1
                        
                        if saved_lines % self.progress_interval == 0:
                            self._report_progress(
                                f"Saving: {saved_lines:,} lines",
                                saved_lines
                            )
            
            message = f"Total: {total_lines:,} | Duplicates: {duplicate_count:,} | Saved (>={min_count}): {saved_lines:,}"
            self._report_progress(message, saved_lines)
            return total_lines, duplicate_count, saved_lines, message
        except FileNotFoundError:
            return 0, 0, 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, 0, 0, f"Error: {str(e)}"
    
    def crack_combo_offline(self, wordlist_file: str, combo_file: str,
                          output_file: str, hash_type: str,
                          separator: str) -> Tuple[int, int, str]:
        """
        Crack hashed combos using a wordlist.
        
        Args:
            wordlist_file: Path to wordlist file
            combo_file: Path to combo file with hashes
            output_file: Path to output file
            hash_type: Hash algorithm (md5, sha1, sha256, etc.)
            separator: Separator in combo file
            
        Returns:
            Tuple of (cracked_count, not_found_count, status_message)
        """
        try:
            # Build hash dictionary
            hash_dict: Dict[str, str] = {}
            with open(wordlist_file, 'r', encoding='latin1', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    try:
                        hashed = getattr(hashlib, hash_type)(password.encode()).hexdigest()
                        hash_dict[hashed] = password
                    except AttributeError:
                        return 0, 0, f"Error: Invalid hash type '{hash_type}'"
            
            self._report_progress(f"Loaded {len(hash_dict):,} passwords", len(hash_dict))
            
            # Crack combo file
            cracked_count = 0
            not_found_count = 0
            processed = 0
            
            with open(combo_file, 'r', encoding='utf-8', errors='ignore') as fi, \
                 open(output_file, 'w', encoding='utf-8', errors='ignore') as fo:
                
                for line in fi:
                    processed += 1
                    if separator in line:
                        parts = line.strip().split(separator)
                        if len(parts) >= 2:
                            username = parts[0]
                            hash_value = parts[1]
                            
                            if hash_value in hash_dict:
                                cracked_count += 1
                                fo.write(f"{username}{separator}{hash_dict[hash_value]}\n")
                                if cracked_count % 100 == 0:
                                    self._report_progress(
                                        f"Cracked: {cracked_count:,}",
                                        cracked_count
                                    )
                            else:
                                not_found_count += 1
                    
                    if processed % self.progress_interval == 0:
                        self._report_progress(
                            f"Processed: {processed:,} | Cracked: {cracked_count:,}",
                            processed
                        )
            
            message = f"Finished: {cracked_count:,} cracked, {not_found_count:,} not found"
            self._report_progress(message, cracked_count)
            return cracked_count, not_found_count, message
        except FileNotFoundError as e:
            return 0, 0, f"Error: File not found - {str(e)}"
        except Exception as e:
            return 0, 0, f"Error: {str(e)}"
    
    def encode_combo(self, input_file: str, output_file: str, hash_type: str,
                    encode_mode: int, separator: str) -> Tuple[int, int, str]:
        """
        Encode passwords or entire lines in a combo file.
        
        Args:
            input_file: Path to input file
            output_file: Path to output file
            hash_type: Hash algorithm (md5, sha1, sha256, etc.)
            encode_mode: Encoding mode
                0: Encode entire line
                1: Encode password (right side of separator)
                2: Encode email/username (left side of separator)
            separator: Separator in combo file
            
        Returns:
            Tuple of (processed_lines, error_count, status_message)
        """
        try:
            processed_lines = 0
            error_count = 0
            
            with open(input_file, 'r', encoding='latin1', errors='ignore') as fi, \
                 open(output_file, 'w', encoding='utf-8', errors='ignore') as fo:
                
                for line in fi:
                    processed_lines += 1
                    line = line.strip()
                    
                    try:
                        if encode_mode == 0:
                            # Encode entire line
                            hashed = getattr(hashlib, hash_type)(line.encode()).hexdigest()
                            fo.write(hashed + '\n')
                        elif encode_mode == 1:
                            # Encode password
                            if separator in line:
                                parts = line.split(separator)
                                username = parts[0]
                                password = separator.join(parts[1:])
                                hashed = getattr(hashlib, hash_type)(password.encode()).hexdigest()
                                fo.write(f"{username}{separator}{hashed}\n")
                            else:
                                error_count += 1
                        elif encode_mode == 2:
                            # Encode username/email
                            if separator in line:
                                parts = line.split(separator)
                                username = parts[0]
                                password = separator.join(parts[1:])
                                hashed = getattr(hashlib, hash_type)(username.encode()).hexdigest()
                                fo.write(f"{hashed}{separator}{password}\n")
                            else:
                                error_count += 1
                    except (AttributeError, IndexError):
                        error_count += 1
                    
                    if processed_lines % self.progress_interval == 0:
                        self._report_progress(
                            f"Processed: {processed_lines:,} lines, Errors: {error_count}",
                            processed_lines
                        )
            
            message = f"Finished: {processed_lines:,} lines processed, {error_count} errors"
            self._report_progress(message, processed_lines)
            return processed_lines, error_count, message
        except FileNotFoundError:
            return 0, 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, 0, f"Error: {str(e)}"
    
    def split_file(self, input_file: str, output_dir: str, lines_per_file: int) -> Tuple[int, int, str]:
        """
        Split a large file into smaller files.
        
        Args:
            input_file: Path to input file
            output_dir: Directory for output files
            lines_per_file: Number of lines per output file
            
        Returns:
            Tuple of (total_lines, file_count, status_message)
        """
        try:
            # Create output directory if it doesn't exist
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            total_lines = 0
            file_count = 0
            current_lines = 0
            
            input_filename = Path(input_file).name
            output_file = None
            
            with open(input_file, 'r', encoding='utf-8', errors='ignore') as fi:
                for line in fi:
                    if current_lines == 0:
                        if output_file:
                            output_file.close()
                        output_path = Path(output_dir) / f"part{file_count}_{input_filename}"
                        output_file = open(output_path, 'w', encoding='utf-8', errors='ignore')
                        self._report_progress(f"Creating part {file_count}", file_count)
                        file_count += 1
                    
                    output_file.write(line)
                    total_lines += 1
                    current_lines += 1
                    
                    if current_lines >= lines_per_file:
                        current_lines = 0
                    
                    if total_lines % self.progress_interval == 0:
                        self._report_progress(
                            f"Processed: {total_lines:,} lines, {file_count} files",
                            total_lines
                        )
            
            if output_file:
                output_file.close()
            
            message = f"Finished: {total_lines:,} lines split into {file_count} files"
            self._report_progress(message, total_lines)
            return total_lines, file_count, message
        except FileNotFoundError:
            return 0, 0, f"Error: File '{input_file}' not found"
        except Exception as e:
            return 0, 0, f"Error: {str(e)}"


def get_available_hash_algorithms() -> List[str]:
    """Get list of available hash algorithms."""
    return sorted([algo for algo in hashlib.algorithms_available if not algo.startswith('shake_')])
