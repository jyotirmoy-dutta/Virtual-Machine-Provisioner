# Handles Vagrant and VirtualBox operations

import os
import subprocess
import shutil
from pathlib import Path

class VagrantManager:
    def __init__(self, work_dir=".vagrant_vms"):
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(exist_ok=True)

    def _vm_dir(self, name):
        return self.work_dir / name

    def _vagrantfile_path(self, name):
        return self._vm_dir(name) / "Vagrantfile"

    def create_vm(self, config):
        """Create VM(s) from config. Handles both single and multi-VM configs."""
        vms = config['vms']
        results = []
        
        for vm in vms:
            name = vm['name']
            vm_dir = self._vm_dir(name)
            vm_dir.mkdir(exist_ok=True)
            vagrantfile = self._vagrantfile_path(name)
            self._write_vagrantfile(vagrantfile, vm)
            # Run 'vagrant up' in the VM directory
            result = self._run_vagrant_cmd(['up'], vm_dir)
            results.append(f"VM '{name}': {result}")
        
        return "\n".join(results)

    def start_vm(self, name):
        return self._run_vagrant_cmd(['up'], self._vm_dir(name))

    def stop_vm(self, name):
        return self._run_vagrant_cmd(['halt'], self._vm_dir(name))

    def destroy_vm(self, name):
        result = self._run_vagrant_cmd(['destroy', '-f'], self._vm_dir(name))
        # Optionally remove the VM directory
        shutil.rmtree(self._vm_dir(name), ignore_errors=True)
        return result

    def list_vms(self):
        vms = []
        for d in self.work_dir.iterdir():
            if d.is_dir() and (d / "Vagrantfile").exists():
                vms.append(d.name)
        return vms

    def status_vm(self, name):
        return self._run_vagrant_cmd(['status'], self._vm_dir(name))

    def _run_vagrant_cmd(self, args, cwd):
        try:
            result = subprocess.run(['vagrant'] + args, cwd=cwd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stdout + "\n" + e.stderr

    def _write_vagrantfile(self, path, vm):
        # Generate a Vagrantfile from the config
        lines = [
            f'Vagrant.configure("2") do |config|',
            f'  config.vm.box = "{vm["box"]}"',
            f'  config.vm.provider "virtualbox" do |vb|',
            f'    vb.memory = "{vm.get("memory", 1024)}"',
            f'    vb.cpus = {vm.get("cpus", 1)}',
            f'  end',
            f'  config.vm.hostname = "{vm["name"]}"',
        ]
        # Networking
        net = vm.get('network', {})
        if net.get('type') == 'nat' and 'forwarded_ports' in net:
            for fp in net['forwarded_ports']:
                lines.append(f'  config.vm.network "forwarded_port", guest: {fp["guest"]}, host: {fp["host"]}')
        # Synced folders
        for folder in vm.get('synced_folders', []):
            lines.append(f'  config.vm.synced_folder "{folder["host"]}", "{folder["guest"]}"')
        # Provisioning
        for prov in vm.get('provision', []):
            if prov['type'] == 'shell':
                lines.append(f'  config.vm.provision "shell", inline: <<-SHELL')
                for line in prov['inline'].splitlines():
                    lines.append(f'    {line}')
                lines.append(f'  SHELL')
        lines.append('end')
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

    # TODO: Implement methods for VM lifecycle, config, etc. 