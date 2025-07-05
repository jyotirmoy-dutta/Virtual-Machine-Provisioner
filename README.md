# 🚀 Virtual Machine Provisioner

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/virtualMachineProvisioner)
[![Vagrant](https://img.shields.io/badge/Vagrant-Required-orange.svg)](https://www.vagrantup.com/)
[![VirtualBox](https://img.shields.io/badge/VirtualBox-Required-blue.svg)](https://www.virtualbox.org/)

> **A robust, cross-platform CLI tool to spin up and manage preconfigured Virtual Machines using VirtualBox and Vagrant**

The Virtual Machine Provisioner is a professional-grade tool designed for developers, DevOps engineers, and system administrators who need to quickly create, manage, and orchestrate virtual machines for development, testing, and deployment scenarios.

## ✨ Features

### 🎯 Core Functionality
- **VM Lifecycle Management**: Create, start, stop, destroy, and monitor VMs
- **Multi-VM Orchestration**: Deploy and manage multiple VMs simultaneously
- **Configuration-Driven**: YAML-based configuration files for reproducible deployments
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux

### 🔧 Advanced Features
- **Network Configuration**: NAT, Bridged, and Host-only networking with port forwarding
- **Shared Folders**: Bidirectional file sharing between host and VMs
- **Automated Provisioning**: Shell script execution for VM setup and configuration
- **Snapshot Management**: Create and restore VM snapshots for backup/rollback
- **SSH Access**: Direct SSH connection to running VMs
- **Progress Indicators**: Real-time feedback during VM operations

### 🛡️ Enterprise Features
- **Dependency Validation**: Automatic detection and validation of required tools
- **Error Handling**: Comprehensive error messages with troubleshooting guidance
- **Configuration Validation**: YAML schema validation with helpful error messages
- **Modular Architecture**: Extensible design for custom plugins and integrations
- **Logging & Monitoring**: Detailed operation logging for debugging and audit trails

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**
- **Vagrant** ([Download](https://www.vagrantup.com/downloads.html))
- **VirtualBox** ([Download](https://www.virtualbox.org/wiki/Downloads))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/virtualMachineProvisioner.git
cd virtualMachineProvisioner

# Install dependencies
python -m pip install -r requirements.txt

# Install as a package (optional)
python -m pip install -e .
```

### Your First VM

```bash
# Create a simple Ubuntu VM
python main.py create examples/ubuntu_vm.yaml

# List managed VMs
python main.py list

# Check VM status
python main.py status ubuntu-test
```

## 📖 Usage

### Basic Commands

```bash
# Create VM(s) from configuration
python main.py create config.yaml

# Start a stopped VM
python main.py start vm-name

# Stop a running VM
python main.py stop vm-name

# Destroy a VM completely
python main.py destroy vm-name

# List all managed VMs
python main.py list

# Check VM status
python main.py status vm-name

# SSH into a VM
python main.py ssh vm-name

# Create a snapshot
python main.py snapshot vm-name snapshot-name

# Restore from snapshot
python main.py restore vm-name snapshot-name
```

### Configuration Examples

#### Single VM Configuration

```yaml
vm:
  name: web-server
  box: ubuntu/bionic64
  memory: 2048
  cpus: 2
  network:
    type: nat
    forwarded_ports:
      - guest: 22
        host: 2222
      - guest: 80
        host: 8080
  synced_folders:
    - host: ./src
      guest: /var/www/app
  provision:
    - type: shell
      inline: |
        apt-get update
        apt-get install -y nginx
        systemctl enable nginx
        systemctl start nginx
```

#### Multi-VM Configuration

```yaml
vms:
  - name: web-server
    box: ubuntu/bionic64
    memory: 2048
    cpus: 2
    network:
      type: nat
      forwarded_ports:
        - guest: 80
          host: 8080
    provision:
      - type: shell
        inline: |
          apt-get update
          apt-get install -y nginx

  - name: db-server
    box: ubuntu/bionic64
    memory: 1024
    cpus: 1
    network:
      type: nat
      forwarded_ports:
        - guest: 3306
          host: 3306
    provision:
      - type: shell
        inline: |
          apt-get update
          apt-get install -y mysql-server
```

## 🏗️ Architecture

```
virtualMachineProvisioner/
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
├── setup.py               # Package installation
├── test_provisioner.py    # Test suite
├── provisioner/           # Core package
│   ├── __init__.py
│   ├── cli.py             # CLI commands and interface
│   ├── vagrant_manager.py # VM lifecycle management
│   ├── config.py          # Configuration parsing & validation
│   └── utils.py           # Utility functions
└── examples/              # Sample configurations
    ├── ubuntu_vm.yaml     # Single Ubuntu VM
    ├── centos_vm.yaml     # Single CentOS VM
    └── multi_vm.yaml      # Multi-VM setup
```

## 🔧 Configuration Reference

### VM Properties

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `name` | string | ✅ | - | Unique VM identifier |
| `box` | string | ✅ | - | Vagrant box name |
| `memory` | integer | ❌ | 1024 | RAM in MB |
| `cpus` | integer | ❌ | 1 | Number of CPU cores |

### Network Configuration

| Property | Type | Description |
|----------|------|-------------|
| `type` | string | Network type: `nat`, `bridged`, `hostonly` |
| `forwarded_ports` | array | Port forwarding rules |

### Synced Folders

| Property | Type | Description |
|----------|------|-------------|
| `host` | string | Path on host machine |
| `guest` | string | Path inside VM |

### Provisioning

| Property | Type | Description |
|----------|------|-------------|
| `type` | string | Provisioning type: `shell` |
| `inline` | string | Shell script content |

## 🎯 Use Cases

### Development Environments
- **Multi-service Applications**: Deploy web, database, and cache servers
- **Testing Environments**: Isolated environments for integration testing
- **CI/CD Pipelines**: Automated VM provisioning for build and test

### Learning and Training
- **Educational Labs**: Pre-configured environments for courses
- **Workshop Setup**: Quick deployment of training environments
- **Proof of Concepts**: Rapid prototyping of infrastructure

### Production-like Testing
- **Staging Environments**: Mirror production configurations
- **Load Testing**: Scalable test environments
- **Disaster Recovery**: Backup and restore testing

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/virtualMachineProvisioner.git
cd virtualMachineProvisioner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
python -m pip install -r requirements.txt

# Install in development mode
python -m pip install -e .
```

### Running Tests

```bash
# Run the test suite
python test_provisioner.py

# Run specific tests
python -c "from test_provisioner import test_imports; test_imports()"
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Documentation

- **[Installation Guide](INSTALL.md)** - Detailed setup instructions
- **[Usage Guide](USAGE.md)** - Comprehensive usage documentation
- **[Configuration Examples](examples/)** - Sample VM configurations

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Ensure cross-platform compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vagrant](https://www.vagrantup.com/) - VM management framework
- [VirtualBox](https://www.virtualbox.org/) - Virtualization platform
- [Click](https://click.palletsprojects.com/) - Python CLI framework
- [Rich](https://rich.readthedocs.io/) - Rich text and formatting library

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/virtualMachineProvisioner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/virtualMachineProvisioner/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/virtualMachineProvisioner/wiki)

## 🚀 Roadmap

- [ ] **Docker Integration**: Support for Docker containers
- [ ] **Cloud Providers**: AWS, Azure, GCP integration
- [ ] **Ansible Provisioning**: Advanced configuration management
- [ ] **GUI Interface**: Web-based management interface
- [ ] **Plugin System**: Extensible architecture for custom providers
- [ ] **Monitoring**: Built-in VM monitoring and metrics
- [ ] **Backup/Restore**: Automated backup strategies
- [ ] **Multi-User Support**: Role-based access control

---

**Made with ❤️ for the DevOps community**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/virtualMachineProvisioner?style=social)](https://github.com/yourusername/virtualMachineProvisioner)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/virtualMachineProvisioner?style=social)](https://github.com/yourusername/virtualMachineProvisioner)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/virtualMachineProvisioner)](https://github.com/yourusername/virtualMachineProvisioner/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/virtualMachineProvisioner)](https://github.com/yourusername/virtualMachineProvisioner/pulls) 