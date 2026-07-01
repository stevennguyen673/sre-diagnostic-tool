from diagnostics.cpu import get_cpu_metrics
from diagnostics.memory import get_memory_metrics
from diagnostics.disk import get_disk_metrics
from diagnostics.network import get_network_metrics

print("========================================")
print("      SRE LOCAL DIAGNOSTICS REPORT      ")
print("========================================\n")

print("CPU / TOP PROCESSES")
print("========================================\n")

cpu = get_cpu_metrics()

for process in cpu:
    print("PID: ", process["pid"])
    print("Command: ", process["command"])
    print("CPU Usage: ", process["cpu_percentage"])
    print("Memory Usage: ", process["memory_percentage"])
    print("\n")

print("MEMORY")
print("========================================\n")

memory = get_memory_metrics()

print("Total: ", memory["total"])
print("Used: ", memory["used"])
print("Available: ", memory["available"])
print("\n")

print("DISK")
print("========================================\n")

disk = get_disk_metrics()

print("Size: ", disk["size"])
print("Used: ", disk["used"])
print("Available: ", disk["available"])
print("Usage: ", disk["usage"])
print("\n")

print("NETWORK")
print("========================================\n")

networks = get_network_metrics()

for network in networks:
    print(f"{network["protocol"].upper()} {network["state"].upper()} {network["local_address"]}") 

print("\n")


print("========================================")
print("   Diagnostics Completed Succesfully   ")
print("========================================\n")

