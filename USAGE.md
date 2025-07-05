# Usage Guide

This guide covers how to use the Virtual Machine Provisioner effectively.

## Quick Start

1. **Create your first VM:**
   ```bash
   python main.py create examples/ubuntu_vm.yaml
   ```

2. **List managed VMs:**
   ```bash
   python main.py list
   ```

3. **Check VM status:**
   ```bash
   python main.py status ubuntu-test
   ```

## CLI Commands

### `create` - Create VM(s) from config file
Creates and starts one or more VMs based on a YAML configuration file.

```bash
python main.py create <config_file>
```

**Options:**
- `--no-progress`: Disable progress indicators

**Examples:**
```bash
# Create a single VM
python main.py create examples/ubuntu_vm.yaml

# Create multiple VMs
python main.py create examples/multi_vm.yaml

# Create without progress bar
python main.py create examples/ubuntu_vm.yaml --no-progress
```

### `start` - Start a VM
Starts a stopped VM by name.

```bash
python main.py start <vm_name>
```

**Example:**
```bash
python main.py start ubuntu-test
```

### `stop` - Stop a VM
Gracefully stops a running VM.

```bash
python main.py stop <vm_name>
```

**Example:**
```bash
python main.py stop ubuntu-test
```

### `destroy` - Destroy a VM
Completely removes a VM and its associated files.

```bash
python main.py destroy <vm_name>
```

**Example:**
```bash
python main.py destroy ubuntu-test
```

### `list` - List managed VMs
Shows all VMs managed by the provisioner.

```bash
python main.py list
```

### `status` - Show VM status
Displays the current status of a specific VM.

```bash
python main.py status <vm_name>
```

**Example:**
```bash
python main.py status ubuntu-test
```

### `ssh` - SSH into a VM
Opens an SSH connection to a running VM.

```bash
python main.py ssh <vm_name>
```

**Example:**
```bash
python main.py ssh ubuntu-test
```

### `snapshot` - Create VM snapshot
Creates a snapshot of a VM for backup/restore purposes.

```bash
python main.py snapshot <vm_name> <snapshot_name>
```

**Example:**
```bash
python main.py snapshot ubuntu-test before-update
```

### `restore` - Restore VM from snapshot
Restores a VM to a previously created snapshot.

```bash
python main.py restore <vm_name> <snapshot_name>
```

**Example:**
```bash
python main.py restore ubuntu-test before-update
```

## Configuration Files

The provisioner uses YAML configuration files to define VM specifications.

### Single VM Configuration

```yaml
vm:
  name: my-vm
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
    - host: ./shared
      guest: /vagrant_data
  provision:
    - type: shell
      inline: |
        echo "Hello from the VM!"
        apt-get update
```

### Multi-VM Configuration

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

## Configuration Options

### VM Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Unique name for the VM |
| `box` | string | Yes | Vagrant box name (e.g., "ubuntu/bionic64") |
| `memory` | integer | No | RAM in MB (default: 1024) |
| `cpus` | integer | No | Number of CPU cores (default: 1) |

### Network Configuration

| Property | Type | Description |
|----------|------|-------------|
| `type` | string | Network type: "nat", "bridged", or "hostonly" |
| `forwarded_ports` | array | List of port forwarding rules |

**Port Forwarding:**
```yaml
forwarded_ports:
  - guest: 22    # Port inside the VM
    host: 2222   # Port on your host machine
```

### Synced Folders

Share directories between your host and the VM:

```yaml
synced_folders:
  - host: ./my-files      # Path on your host
    guest: /home/vagrant  # Path inside the VM
```

### Provisioning

Automate VM setup with shell scripts:

```yaml
provision:
  - type: shell
    inline: |
      apt-get update
      apt-get install -y nginx
      systemctl enable nginx
      systemctl start nginx
```

## Popular Boxes

### Ubuntu
- `ubuntu/bionic64` - Ubuntu 18.04 LTS
- `ubuntu/focal64` - Ubuntu 20.04 LTS
- `ubuntu/jammy64` - Ubuntu 22.04 LTS

### CentOS
- `centos/7` - CentOS 7
- `centos/8` - CentOS 8
- `centos/stream8` - CentOS Stream 8

### Windows
- `gusztavvargadr/windows-10` - Windows 10
- `gusztavvargadr/windows-server` - Windows Server

### Other
- `debian/buster64` - Debian 10
- `fedora/32-cloud-base` - Fedora 32
- `opensuse/Leap-15.2.x86_64` - openSUSE Leap 15.2

## Best Practices

### 1. Use Descriptive Names
```yaml
vm:
  name: web-server-prod  # Good
  # name: vm1           # Bad
```

### 2. Plan Resource Allocation
```yaml
vm:
  memory: 2048  # 2GB RAM
  cpus: 2       # 2 CPU cores
```

### 3. Use Port Forwarding for Services
```yaml
network:
  forwarded_ports:
    - guest: 80
      host: 8080    # Access web server at localhost:8080
    - guest: 3306
      host: 3306    # Access MySQL at localhost:3306
```

### 4. Organize Synced Folders
```yaml
synced_folders:
  - host: ./src
    guest: /var/www/app
  - host: ./config
    guest: /etc/app
```

### 5. Use Idempotent Provisioning
```yaml
provision:
  - type: shell
    inline: |
      if ! command -v nginx &> /dev/null; then
        apt-get update
        apt-get install -y nginx
      fi
```

## Troubleshooting

### Common Issues

**VM won't start:**
1. Check if VirtualBox is running
2. Verify virtualization is enabled in BIOS
3. Check available system resources

**Port forwarding not working:**
1. Ensure the port isn't already in use
2. Check firewall settings
3. Verify the service is running in the VM

**Synced folders not working:**
1. Check file permissions
2. Ensure the host path exists
3. Verify VirtualBox Guest Additions are installed

**Provisioning fails:**
1. Check the script syntax
2. Ensure the VM has internet access
3. Verify package names and commands

### Getting Help

1. Check VM status: `python main.py status <vm_name>`
2. View Vagrant logs: Check the `.vagrant_vms/<vm_name>` directory
3. SSH into the VM: `python main.py ssh <vm_name>`
4. Check VirtualBox GUI for VM details

## Advanced Usage

### Custom Vagrantfile Generation

The provisioner automatically generates Vagrantfiles, but you can customize them by editing the generated files in `.vagrant_vms/<vm_name>/Vagrantfile`.

### Plugin System

The modular design allows for easy extension. You can add new provisioning types, network configurations, or VM providers by extending the appropriate classes.

### Integration with CI/CD

The provisioner can be integrated into CI/CD pipelines for automated testing and deployment:

```bash
# In your CI script
python main.py create test-vm.yaml
python main.py ssh test-vm "run-tests.sh"
python main.py destroy test-vm
``` 