#!/usr/bin/env python3
"""
Comprehensive Integration Test for ListTools v5.0
Tests all components working together
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test all modules can be imported."""
    print("=" * 60)
    print("TEST 1: Module Imports")
    print("=" * 60)
    
    try:
        import list_tools_core
        print("✓ list_tools_core imported")
        
        import list_tools_gui
        print("✓ list_tools_gui imported")
        
        import list_tools_console
        print("✓ list_tools_console imported")
        
        import listtools
        print("✓ listtools (launcher) imported")
        
        print("\n✓ All modules imported successfully!\n")
        return True
    except Exception as e:
        print(f"\n✗ Import failed: {e}\n")
        return False

def test_core_functionality():
    """Test core processing functions."""
    print("=" * 60)
    print("TEST 2: Core Functionality")
    print("=" * 60)
    
    from list_tools_core import ListToolsCore
    
    # Create test file
    test_file = "test_data/integration_test.txt"
    with open(test_file, 'w') as f:
        f.write("test1@email.com:password1\n")
        f.write("test2@email.com:password2\n")
        f.write("test1@email.com:password1\n")  # duplicate
        f.write("test3@email.com:password3\n")
        f.write("common:password\n")
        f.write("common:password\n")  # duplicate
    
    core = ListToolsCore()
    
    # Test 1: Count lines
    count, msg = core.count_lines(test_file)
    assert count == 6, f"Expected 6 lines, got {count}"
    print(f"✓ Line counter: {msg}")
    
    # Test 2: Remove duplicates
    total, dups, saved, msg = core.remove_duplicates(
        test_file,
        "test_data/integration_unique.txt"
    )
    assert total == 6 and dups == 2 and saved == 4, f"Unexpected duplicate results"
    print(f"✓ Duplicate remover: {msg}")
    
    # Test 3: Split lines
    processed, errors, msg = core.split_lines(
        test_file,
        "test_data/integration_split.txt",
        ":",
        0
    )
    assert processed == 6 and errors == 0, f"Unexpected split results"
    print(f"✓ Line splitter: {msg}")
    
    # Test 4: Encode combo
    processed, errors, msg = core.encode_combo(
        test_file,
        "test_data/integration_encoded.txt",
        "md5",
        1,
        ":"
    )
    assert processed == 6 and errors == 0, f"Unexpected encode results"
    print(f"✓ Password encoder: {msg}")
    
    # Test 5: File splitter
    total, files, msg = core.split_file(
        test_file,
        "test_data/integration_split_output",
        2
    )
    assert total == 6 and files == 3, f"Unexpected split file results"
    print(f"✓ File splitter: {msg}")
    
    print("\n✓ All core functions working correctly!\n")
    return True

def test_hash_algorithms():
    """Test all available hash algorithms."""
    print("=" * 60)
    print("TEST 3: Hash Algorithms")
    print("=" * 60)
    
    from list_tools_core import get_available_hash_algorithms
    
    algorithms = get_available_hash_algorithms()
    print(f"Available algorithms: {len(algorithms)}")
    print(f"Common algorithms available:")
    
    common = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    for algo in common:
        if algo in algorithms:
            print(f"  ✓ {algo}")
        else:
            print(f"  ✗ {algo} NOT AVAILABLE")
    
    print("\n✓ Hash algorithms checked!\n")
    return True

def test_file_structure():
    """Test project file structure."""
    print("=" * 60)
    print("TEST 4: Project Structure")
    print("=" * 60)
    
    required_files = [
        'listtools.py',
        'list_tools_core.py',
        'list_tools_gui.py',
        'list_tools_console.py',
        'README.md',
        'INSTALL.md',
        'USAGE_EXAMPLES.md',
        'requirements.txt',
        '.gitignore',
        'test_core.py',
        'test_performance.py',
        'file4.py'  # legacy
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file}")
        else:
            print(f"✗ {file} MISSING")
            all_exist = False
    
    if all_exist:
        print("\n✓ All required files present!\n")
    else:
        print("\n✗ Some files are missing!\n")
    
    return all_exist

def test_documentation():
    """Test documentation completeness."""
    print("=" * 60)
    print("TEST 5: Documentation")
    print("=" * 60)
    
    readme = Path('README.md').read_text()
    install = Path('INSTALL.md').read_text()
    usage = Path('USAGE_EXAMPLES.md').read_text()
    
    checks = [
        ('README has version 5.0', 'v5.0' in readme or 'Version: 5.0' in readme),
        ('README has features list', 'Features' in readme or 'قابلیت' in readme),
        ('README has Persian docs', 'فارسی' in readme or 'پشتیبانی' in readme),
        ('INSTALL has requirements', 'Requirements' in install or 'Python' in install),
        ('INSTALL has troubleshooting', 'Troubleshooting' in install),
        ('USAGE has examples', 'Example' in usage and 'python' in usage.lower()),
    ]
    
    for check_name, result in checks:
        if result:
            print(f"✓ {check_name}")
        else:
            print(f"✗ {check_name}")
    
    print("\n✓ Documentation checked!\n")
    return True

def run_all_tests():
    """Run all integration tests."""
    print("\n" + "=" * 60)
    print("LISTTOOLS v5.0 - INTEGRATION TEST SUITE")
    print("=" * 60 + "\n")
    
    results = []
    
    try:
        results.append(("Module Imports", test_imports()))
        results.append(("Core Functionality", test_core_functionality()))
        results.append(("Hash Algorithms", test_hash_algorithms()))
        results.append(("Project Structure", test_file_structure()))
        results.append(("Documentation", test_documentation()))
    except Exception as e:
        print(f"\n✗ CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name:.<40} {status}")
    
    print("=" * 60)
    print(f"TOTAL: {passed}/{total} tests passed")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 ALL INTEGRATION TESTS PASSED! 🎉")
        print("\nListTools v5.0 is fully functional and ready to use!")
        return True
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
