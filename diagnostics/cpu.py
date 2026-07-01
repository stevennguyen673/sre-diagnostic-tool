import subprocess

def get_cpu_metrics():
    res = subprocess.run(["ps", "aux", "--sort=-%cpu"], capture_output=True, text=True)

    cleaned = res.stdout.split("\n", maxsplit=5)[:6]

    # holds top 5 processes based on cpu usage
    top_processes = []

    for line in cleaned:
        line_list = line.split()
        # skips header
        if line_list[0] == "USER":
            continue
        else:
            process = {}
            process["pid"] = line_list[1]
            process["cpu_percentage"] = line_list[2]
            process["memory_percentage"] = line_list[3]
            
            # get more readable name than path
            command_name_path_list = line_list[10].split("/")
            command_name = command_name_path_list[-1]
            
            process["command"] = command_name

            top_processes.append(process)
    
    return top_processes


