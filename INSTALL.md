# Installation Guide

This guide will help you install all the required dependencies for the Virtual Machine Provisioner.

## Prerequisites

- Python 3.7 or higher
- Administrator/sudo access (for installing VirtualBox and Vagrant)

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

### macOS
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Linux (CentOS/RHEL)
```bash
sudo yum install python3 python3-pip
```

## Step 2: Install VirtualBox

### Windows
1. Download from [VirtualBox Downloads](https://www.virtualbox.org/wiki/Downloads)
2. Run the installer
3. Restart your computer if prompted

### macOS
```bash
brew install virtualbox
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install virtualbox
```

### Linux (CentOS/RHEL)
```bash
sudo yum install VirtualBox
```

## Step 3: Install Vagrant

### Windows
1. Download from [Vagrant Downloads](https://www.vagrantup.com/downloads.html)
2. Run the installer
3. Restart your terminal/command prompt

### macOS
```bash
brew install vagrant
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install vagrant
```

### Linux (CentOS/RHEL)
```bash
sudo yum install vagrant
```

## Step 4: Install the Virtual Machine Provisioner

### Option 1: Install from source
```bash
git clone https://github.com/yourusername/virtualMachineProvisioner.git
cd virtualMachineProvisioner
python -m pip install -r requirements.txt
```

### Option 2: Install as a package (after setup.py is configured)
```bash
python -m pip install -e .
```

## Step 5: Verify Installation

Run these commands to verify everything is installed correctly:

```bash
python --version
vagrant --version
VBoxManage --version
python main.py --help
```

## Troubleshooting

### VirtualBox Installation Issues

**Windows:**
- Ensure virtualization is enabled in BIOS
- Install the latest version from the official website
- Run as administrator if needed

**macOS:**
- Allow VirtualBox in System Preferences > Security & Privacy
- Install the latest version for your macOS version

**Linux:**
- Install VirtualBox Extension Pack for USB support
- Add your user to the vboxusers group: `sudo usermod -a -G vboxusers $USER`

### Vagrant Installation Issues

**Common Issues:**
- Ensure VirtualBox is installed before Vagrant
- Restart your terminal after installation
- Check PATH environment variable

### Python Issues

**Windows:**
- Ensure Python is added to PATH during installation
- Use `python -m pip` instead of `pip` if needed

**Linux/macOS:**
- Use `python3` and `pip3` if `python` points to Python 2

## Next Steps

After installation, you can:

1. Create your first VM:
   ```bash
   python main.py create examples/ubuntu_vm.yaml
   ```

2. List managed VMs:
   ```bash
   python main.py list
   ```

3. Get help:
   ```bash
   python main.py --help
   ```

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Check the [Vagrant documentation](https://www.vagrantup.com/docs)
4. Check the [VirtualBox documentation](https://www.virtualbox.org/manual/) 