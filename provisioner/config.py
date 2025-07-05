# Handles config file parsing and validation

import yaml
import os

def load_config(path):
    """Load and validate a VM config from a YAML file."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error: {e}")
    
    # Check if it's a single VM or multi-VM config
    if 'vm' in config:
        # Single VM config
        validate_vm_config(config['vm'])
        return {'vms': [config['vm']]}
    elif 'vms' in config:
        # Multi-VM config
        for vm in config['vms']:
            validate_vm_config(vm)
        return config
    else:
        raise ValueError("Config must contain either 'vm' or 'vms' section.")
    
    return config

def validate_vm_config(vm):
    """Validate a single VM configuration."""
    required = ['name', 'box']
    for field in required:
        if field not in vm:
            raise ValueError(f"Missing required VM field: {field}")
    
    # Validate network configuration
    if 'network' in vm:
        net = vm['network']
        if 'type' not in net:
            raise ValueError("Network configuration must specify 'type'")
        if net['type'] not in ['nat', 'bridged', 'hostonly']:
            raise ValueError("Network type must be 'nat', 'bridged', or 'hostonly'")
        
        if 'forwarded_ports' in net:
            for fp in net['forwarded_ports']:
                if 'guest' not in fp or 'host' not in fp:
                    raise ValueError("Forwarded ports must specify 'guest' and 'host'")
    
    # Validate synced folders
    if 'synced_folders' in vm:
        for folder in vm['synced_folders']:
            if 'host' not in folder or 'guest' not in folder:
                raise ValueError("Synced folders must specify 'host' and 'guest'")
    
    # Validate provisioning
    if 'provision' in vm:
        for prov in vm['provision']:
            if 'type' not in prov:
                raise ValueError("Provisioning must specify 'type'")
            if prov['type'] == 'shell' and 'inline' not in prov:
                raise ValueError("Shell provisioning must specify 'inline' script") 