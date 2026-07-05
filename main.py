from diagnostics.cpu import get_cpu_metrics
from diagnostics.memory import get_memory_metrics
from diagnostics.disk import get_disk_metrics
from diagnostics.network import get_network_metrics
from azure.teardown import teardown
from azure.deploy import deploy_vm

print("===== SRE LOCAL DIAGNOSTICS REPORT =====\n")

print("--- CPU (Top 5 Processes) ---\n")

cpu = get_cpu_metrics()

for process in cpu:
    print("PID: ", process["pid"])
    print("Command: ", process["command"])
    print("CPU Usage: ", process["cpu_percentage"] + "%")
    print("Memory Usage: ", process["memory_percentage"] + "%")
    print("\n")

print("--- MEMORY ---\n")

memory = get_memory_metrics()

print("Total: ", memory["total"])
print("Used: ", memory["used"])
print("Available: ", memory["available"])
print("\n")

print("--- DISK ---\n")

disk = get_disk_metrics()

print("Size: ", disk["size"])
print("Used: ", disk["used"])
print("Available: ", disk["available"])
print("Usage: ", disk["usage"])
print("\n")

print("--- NETWORK ---\n")

networks = get_network_metrics()

for network in networks:
    print(f"{network["protocol"].upper()} {network["state"].upper()} {network["local_address"]}") 

print("\n")


print("===== Diagnostics Completed Succesfully =====\n")

# Deploy VM
while True:
    response = input("Would you like to deploy a VM? (y/n)")

    if response.lower() == 'y':
        deploy_vm()
        print("Deployment Complete")
        
        while True:
            ans = input("Would you like to teardown now? (y/n)")
            
            if ans.lower() == 'y':
                teardown()
                break
            elif ans.lower() == 'n':
                print("\nRemember to teardown to avoid unwanted charges!!!")
                break
            else:
                print("Invalid input. Try again\n")
        break
    elif response.lower() == 'n':
        print("\nDeployment Cancelled")
        break
    else:
        print("Invalid input. Try again\n")



