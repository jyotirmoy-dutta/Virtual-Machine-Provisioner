import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from provisioner.vagrant_manager import VagrantManager
from provisioner.config import load_config
from provisioner.utils import validate_environment
import subprocess

console = Console()
vagrant = VagrantManager()

@click.group()
def main():
    """Virtual Machine Provisioner CLI"""
    pass

@main.command()
@click.argument('config', type=click.Path(exists=True))
@click.option('--no-progress', is_flag=True, help='Disable progress indicators')
def create(config, no_progress):
    """Create VM(s) from config file."""
    try:
        validate_environment()
        cfg = load_config(config)
        
        if not no_progress:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                task = progress.add_task("Creating VM(s)...", total=None)
                output = vagrant.create_vm(cfg)
                progress.update(task, description="VM(s) created successfully!")
        else:
            output = vagrant.create_vm(cfg)
        
        console.print(f"[green]VM(s) created and started successfully![/green]")
        console.print(output)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
def start(name):
    """Start a VM by name."""
    try:
        validate_environment()
        output = vagrant.start_vm(name)
        console.print(f"[green]VM '{name}' started.[/green]")
        console.print(output)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
def stop(name):
    """Stop a VM by name."""
    try:
        validate_environment()
        output = vagrant.stop_vm(name)
        console.print(f"[yellow]VM '{name}' stopped.[/yellow]")
        console.print(output)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
def destroy(name):
    """Destroy a VM by name."""
    try:
        validate_environment()
        if click.confirm(f"Are you sure you want to destroy VM '{name}'?"):
            output = vagrant.destroy_vm(name)
            console.print(f"[red]VM '{name}' destroyed.[/red]")
            console.print(output)
        else:
            console.print("[yellow]Operation cancelled.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
def list():
    """List all managed VMs."""
    vms = vagrant.list_vms()
    if vms:
        console.print("[blue]Managed VMs:[/blue]")
        for vm in vms:
            console.print(f"- {vm}")
    else:
        console.print("[yellow]No VMs found.[/yellow]")

@main.command()
@click.argument('name')
def status(name):
    """Show status of a VM by name."""
    try:
        validate_environment()
        output = vagrant.status_vm(name)
        console.print(f"[cyan]Status for VM '{name}':[/cyan]")
        console.print(output)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
def ssh(name):
    """SSH into a VM by name."""
    try:
        validate_environment()
        console.print(f"[green]Connecting to VM '{name}' via SSH...[/green]")
        # Note: This will open an interactive SSH session
        subprocess.run(['vagrant', 'ssh'], cwd=vagrant._vm_dir(name))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
@click.argument('snapshot_name')
def snapshot(name, snapshot_name):
    """Create a snapshot of a VM."""
    try:
        validate_environment()
        output = vagrant._run_vagrant_cmd(['snapshot', 'save', snapshot_name], vagrant._vm_dir(name))
        console.print(f"[green]Snapshot '{snapshot_name}' created for VM '{name}'.[/green]")
        console.print(output)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('name')
@click.argument('snapshot_name')
def restore(name, snapshot_name):
    """Restore a VM from a snapshot."""
    try:
        validate_environment()
        if click.confirm(f"Are you sure you want to restore VM '{name}' from snapshot '{snapshot_name}'?"):
            output = vagrant._run_vagrant_cmd(['snapshot', 'restore', snapshot_name], vagrant._vm_dir(name))
            console.print(f"[green]VM '{name}' restored from snapshot '{snapshot_name}'.[/green]")
            console.print(output)
        else:
            console.print("[yellow]Operation cancelled.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]") 