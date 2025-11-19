#!/usr/bin/env python3
"""Test script for ListTools core functionality"""

from list_tools_core import ListToolsCore

def test_line_counter():
    print("Testing Line Counter...")
    core = ListToolsCore()
    count, msg = core.count_lines("test_data/test_combo.txt")
    print(f"  Result: {msg}")
    assert count == 5, f"Expected 5 lines, got {count}"
    print("  ✓ PASSED\n")

def test_line_splitter():
    print("Testing Line Splitter...")
    core = ListToolsCore()
    processed, errors, msg = core.split_lines(
        "test_data/test_combo.txt",
        "test_data/output_split.txt",
        ":",
        0  # Get left part (email)
    )
    print(f"  Result: {msg}")
    assert processed == 5, f"Expected 5 processed, got {processed}"
    print("  ✓ PASSED\n")

def test_duplicate_remover():
    print("Testing Duplicate Remover...")
    core = ListToolsCore()
    total, dups, saved, msg = core.remove_duplicates(
        "test_data/test_combo.txt",
        "test_data/output_unique.txt"
    )
    print(f"  Result: {msg}")
    assert total == 5, f"Expected 5 total, got {total}"
    assert dups == 1, f"Expected 1 duplicate, got {dups}"
    assert saved == 4, f"Expected 4 saved, got {saved}"
    print("  ✓ PASSED\n")

def test_duplicate_saver():
    print("Testing Duplicate Saver...")
    core = ListToolsCore()
    total, dups, saved, msg = core.save_duplicates(
        "test_data/test_combo.txt",
        "test_data/output_dups.txt",
        2  # Save lines appearing >= 2 times
    )
    print(f"  Result: {msg}")
    assert total == 5, f"Expected 5 total, got {total}"
    assert saved == 1, f"Expected 1 saved (duplicate), got {saved}"
    print("  ✓ PASSED\n")

def test_password_encoder():
    print("Testing Password Encoder...")
    core = ListToolsCore()
    processed, errors, msg = core.encode_combo(
        "test_data/test_combo.txt",
        "test_data/output_encoded.txt",
        "md5",
        1,  # Encode password
        ":"
    )
    print(f"  Result: {msg}")
    assert processed == 5, f"Expected 5 processed, got {processed}"
    print("  ✓ PASSED\n")

def test_file_splitter():
    print("Testing File Splitter...")
    core = ListToolsCore()
    total, file_count, msg = core.split_file(
        "test_data/test_combo.txt",
        "test_data/split_output",
        2  # 2 lines per file
    )
    print(f"  Result: {msg}")
    assert total == 5, f"Expected 5 total, got {total}"
    assert file_count == 3, f"Expected 3 files, got {file_count}"
    print("  ✓ PASSED\n")

if __name__ == "__main__":
    print("=" * 60)
    print("ListTools Core Functionality Tests")
    print("=" * 60 + "\n")
    
    try:
        test_line_counter()
        test_line_splitter()
        test_duplicate_remover()
        test_duplicate_saver()
        test_password_encoder()
        test_file_splitter()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
