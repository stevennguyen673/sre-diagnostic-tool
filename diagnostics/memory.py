import subprocess

res = subprocess.run(["free", "-h"], capture_output=True, text=True)\

cleaned = res.stdout.split("\n")

memory = {}

# memory row
line = cleaned[1].split()

memory["total"] = line[1]
memory["used"] = line[2]
memory["available"] = line[-1]
   
    

print(cleaned)
print(memory)