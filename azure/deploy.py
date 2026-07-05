import subprocess
import sys

def run_az_command(command_list):
    """Utility function to safely execute an Azure CLI command array"""
    print(f"Executing: {' '.join(command_list)}")
    try:
        result = subprocess.run(command_list, check=True, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Command failed with return code {e.returncode}!", file=sys.stderr)
        print(f"Details: {e.stderr}", file=sys.stderr)
        sys.exit(1)

def deploy_vm():
    print("=== Azure SRE Diagnostic Automated VM Pipeline ===\n")

    # Capture user inputs
    rg_name = input("Enter Resource Group [rg-sre-prod-01]: ").strip() or "rg-sre-prod-01"
    vm_name = input("Enter VM Name [vm-sre-prod-01]: ").strip() or "vm-sre-prod-01"

    # hardcode to ensure free
    location = "CanadaEast"


    print(f"\nConfiguration:")
    print(f"- Resource Group: {rg_name}")
    print(f"- VM Name: {vm_name}")
    print(f"- Location: {location}\n")

    # Create Resource Group
    print("=== Ensuring Resource Group Exists ===")
    create_rg_cmd = ["az", "group", "create", "--name", rg_name, "--location", location, "--output", "table"]
    run_az_command(create_rg_cmd)

    # Create VM
    check_vm_cmd = ["az", "vm", "list", "-g", rg_name, "--query", f"[?name=='{vm_name}'].name", "-o", "tsv"]
    vm_check_output = run_az_command(check_vm_cmd).strip()
    if not vm_check_output:
        print(f"VM {vm_name} not found. Provisioning now...")
        create_vm_cmd = [
            "az", "vm", "create", 
            "--resource-group", rg_name,
            "--name", vm_name,
            "--image", "Ubuntu2204",
            "--size", "Standard_B2ats_v2",
            "--storage-sku", "Standard_LRS",
            "--admin-username", "azureuser",
            "--generate-ssh-keys",
            "--location", location,
            "--output", "table"
        ]
        run_az_command(create_vm_cmd)

        # Configues Auto-Shutdown
        auto_shutdown_cmd = [
            "az", "vm", "auto-shutdown", 
            "--resource-group", rg_name,
            "--name", vm_name,
            "--time", '2200', # 6pm est
            "--output", "table"    
        ]
        run_az_command(auto_shutdown_cmd)

    else:
        print(f"VM {vm_name} already exists")
    
    