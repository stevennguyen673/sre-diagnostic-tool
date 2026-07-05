from azure.deploy import run_az_command

def teardown():
    rg_name = input(f"What Resource Group do you want to delete?")
    
    while True:
        response = input(f"Are you sure you want to delete Resource Group {rg_name}? (y/n)")
        
        if response.lower() == 'y':
            print("=== Tearing down resources... ===")
            
            delete_cmd = ["az", "group", "delete", "--name", rg_name, "--no-wait", "--yes"]
            run_az_command(delete_cmd)

            print(f"\nSuccessfully Deleted")
            break
        elif response.lower() == 'n':
            print("Deletion Cancelled")
            break
        else:
            print("Invalid input. Try Again\n")
            
    