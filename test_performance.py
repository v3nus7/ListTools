#!/usr/bin/env python3
"""Performance test for ListTools with larger dataset"""

import time
from list_tools_core import ListToolsCore

def create_large_test_file(filename, lines=10000):
    """Create a test file with specified number of lines."""
    print(f"Creating test file with {lines:,} lines...")
    with open(filename, 'w') as f:
        for i in range(lines):
            # Create variety of data including duplicates
            if i % 1000 == 0:
                f.write(f"common@email.com:password123\n")
            elif i % 500 == 0:
                f.write(f"frequent@email.com:test456\n")
            else:
                f.write(f"user{i}@email.com:pass{i}\n")
    print(f"✓ Created {filename}")

def test_performance():
    """Test performance with larger dataset."""
    test_file = "test_data/large_test.txt"
    create_large_test_file(test_file, 10000)
    
    core = ListToolsCore()
    
    # Test 1: Line Counter
    print("\n" + "="*60)
    print("Test 1: Line Counter Performance")
    print("="*60)
    start = time.time()
    count, msg = core.count_lines(test_file)
    elapsed = time.time() - start
    print(f"Result: {msg}")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Speed: {count/elapsed:.0f} lines/second")
    
    # Test 2: Duplicate Remover
    print("\n" + "="*60)
    print("Test 2: Duplicate Remover Performance")
    print("="*60)
    start = time.time()
    total, dups, saved, msg = core.remove_duplicates(
        test_file, 
        "test_data/perf_unique.txt"
    )
    elapsed = time.time() - start
    print(f"Result: {msg}")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Speed: {total/elapsed:.0f} lines/second")
    
    # Test 3: Line Splitter
    print("\n" + "="*60)
    print("Test 3: Line Splitter Performance")
    print("="*60)
    start = time.time()
    processed, errors, msg = core.split_lines(
        test_file,
        "test_data/perf_split.txt",
        ":",
        0
    )
    elapsed = time.time() - start
    print(f"Result: {msg}")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Speed: {processed/elapsed:.0f} lines/second")
    
    # Test 4: Password Encoder
    print("\n" + "="*60)
    print("Test 4: Password Encoder Performance")
    print("="*60)
    start = time.time()
    processed, errors, msg = core.encode_combo(
        test_file,
        "test_data/perf_encoded.txt",
        "md5",
        1,
        ":"
    )
    elapsed = time.time() - start
    print(f"Result: {msg}")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Speed: {processed/elapsed:.0f} lines/second")
    
    print("\n" + "="*60)
    print("PERFORMANCE TESTS COMPLETED!")
    print("="*60)

if __name__ == "__main__":
    test_performance()
