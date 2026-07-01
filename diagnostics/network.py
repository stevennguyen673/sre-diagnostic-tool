import subprocess

def get_network_metrics():

    res = subprocess.run(["ss", "-tuln"], capture_output=True, text=True)

    cleaned = res.stdout.split("\n")

    networks = []

    for line in cleaned:
        if line.strip():
            line_list = line.split()
            # skips header
            if line_list[0] == "Netid":
                continue
            else:
                network = {}
                network["protocol"] = line_list[0]
                network["state"] = line_list[1]
                network["local_address"] = line_list[4]

                networks.append(network)

    return networks
