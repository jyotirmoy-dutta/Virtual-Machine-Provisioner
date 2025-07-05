# Utility functions for the provisioner 

import subprocess
import shutil
import platform

def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []
    
    # Check Vagrant
    if not shutil.which('vagrant'):
        missing.append('Vagrant')
    
    # Check VirtualBox
    if not shutil.which('VBoxManage'):
        missing.append('VirtualBox')
    
    return missing

def get_installation_instructions():
    """Get installation instructions for missing dependencies."""
    system = platform.system().lower()
    
    instructions = {
        'Vagrant': {
            'windows': 'Download from https://www.vagrantup.com/downloads.html',
            'darwin': 'brew install vagrant',
            'linux': 'sudo apt-get install vagrant  # Ubuntu/Debian\nsudo yum install vagrant  # CentOS/RHEL'
        },
        'VirtualBox': {
            'windows': 'Download from https://www.virtualbox.org/wiki/Downloads',
            'darwin': 'brew install virtualbox',
            'linux': 'sudo apt-get install virtualbox  # Ubuntu/Debian\nsudo yum install VirtualBox  # CentOS/RHEL'
        }
    }
    
    return instructions

def validate_environment():
    """Validate that all required dependencies are available."""
    missing = check_dependencies()
    if missing:
        instructions = get_installation_instructions()
        system = platform.system().lower()
        
        error_msg = f"Missing required dependencies: {', '.join(missing)}\n\n"
        error_msg += "Installation instructions:\n"
        
        for dep in missing:
            if dep in instructions and system in instructions[dep]:
                error_msg += f"\n{dep}:\n{instructions[dep][system]}\n"
            else:
                error_msg += f"\n{dep}: Please visit the official website for installation instructions.\n"
        
        raise RuntimeError(error_msg)
    
    return True 