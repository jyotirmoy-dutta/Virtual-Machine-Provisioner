#!/usr/bin/env python3
"""
Test script for the Virtual Machine Provisioner
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    try:
        import click
        print("✓ Click imported successfully")
    except ImportError as e:
        print(f"✗ Click import failed: {e}")
        return False
    
    try:
        from rich.console import Console
        print("✓ Rich imported successfully")
    except ImportError as e:
        print(f"✗ Rich import failed: {e}")
        return False
    
    try:
        import yaml
        print("✓ PyYAML imported successfully")
    except ImportError as e:
        print(f"✗ PyYAML import failed: {e}")
        return False
    
    try:
        from provisioner.vagrant_manager import VagrantManager
        print("✓ VagrantManager imported successfully")
    except ImportError as e:
        print(f"✗ VagrantManager import failed: {e}")
        return False
    
    try:
        from provisioner.config import load_config
        print("✓ Config module imported successfully")
    except ImportError as e:
        print(f"✗ Config module import failed: {e}")
        return False
    
    return True

def test_dependencies():
    """Test if external dependencies are available."""
    print("\nTesting external dependencies...")
    
    import shutil
    
    # Test Vagrant
    if shutil.which('vagrant'):
        print("✓ Vagrant found in PATH")
    else:
        print("✗ Vagrant not found in PATH")
        return False
    
    # Test VirtualBox
    if shutil.which('VBoxManage'):
        print("✓ VirtualBox found in PATH")
    else:
        print("✗ VirtualBox not found in PATH")
        return False
    
    return True

def test_config_parsing():
    """Test config file parsing."""
    print("\nTesting config parsing...")
    
    from provisioner.config import load_config
    
    # Test single VM config
    try:
        config = load_config('examples/ubuntu_vm.yaml')
        print("✓ Single VM config parsed successfully")
    except Exception as e:
        print(f"✗ Single VM config parsing failed: {e}")
        return False
    
    # Test multi-VM config
    try:
        config = load_config('examples/multi_vm.yaml')
        print("✓ Multi-VM config parsed successfully")
    except Exception as e:
        print(f"✗ Multi-VM config parsing failed: {e}")
        return False
    
    return True

def test_vagrant_manager():
    """Test VagrantManager initialization."""
    print("\nTesting VagrantManager...")
    
    from provisioner.vagrant_manager import VagrantManager
    
    try:
        vm_manager = VagrantManager()
        print("✓ VagrantManager initialized successfully")
        
        # Test listing VMs (should work even if no VMs exist)
        vms = vm_manager.list_vms()
        print(f"✓ List VMs works (found {len(vms)} VMs)")
        
    except Exception as e:
        print(f"✗ VagrantManager test failed: {e}")
        return False
    
    return True

def test_cli():
    """Test CLI functionality."""
    print("\nTesting CLI...")
    
    try:
        from main import main
        print("✓ CLI module imported successfully")
    except Exception as e:
        print(f"✗ CLI import failed: {e}")
        return False
    
    return True

def main():
    """Run all tests."""
    print("Virtual Machine Provisioner - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Dependencies", test_dependencies),
        ("Config Parsing", test_config_parsing),
        ("VagrantManager", test_vagrant_manager),
        ("CLI", test_cli),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"✗ {test_name} test failed")
        except Exception as e:
            print(f"✗ {test_name} test failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The provisioner is ready to use.")
        return 0
    else:
        print("❌ Some tests failed. Please check the installation.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 