import subprocess

res = subprocess.run(["ps", "aux", "--sort=-%cpu"], capture_output=True, text=True)

cleaned = res.stdout.split("\n", maxsplit=5)

# holds top 5 processes based on cpu usage
top_processes = []

for output in cleaned:
    output_list = output.split()
    # skips header
    if output_list[0] == "USER":
        continue
    else:
        process = {}
        process["pid"] = output_list[1]
        process["cpu_percentage"] = output_list[2]
        process["memory_percentage"] = output_list[3]
        
        # get more readable name then path
        command_name_path_list = output_list[10].split("/")
        command_name = command_name_path_list[-1]
        
        process["command"] = command_name

        top_processes.append(process)



print(repr(cleaned))
print(top_processes)


