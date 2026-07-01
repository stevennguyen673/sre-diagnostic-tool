import subprocess

def get_disk_metrics():
    res = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)\

    cleaned = res.stdout.split("\n")

    disk = {}

    # memory row
    line = cleaned[1].split()

    disk["size"] = line[1]
    disk["used"] = line[2]
    disk["available"] = line[3]
    disk["usage"] = line[4]

    return disk
   
    

