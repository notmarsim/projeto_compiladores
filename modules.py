import subprocess
import socket

# nmap
def scan_tcp(host="127.0.0.1"):

    if type(host)!= list:
        host = [host]
    ports = []
    for h in host:
        print(f"[+] Running NMAP TCP scan on {h}...")
        result = subprocess.check_output(["nmap","-F", "--open", h, "-oG", "-"]).decode()

        for line in result.splitlines():
            if "Ports:" in line:
                fields = line.split("Ports:")[1].split(",")
                for f in fields:
                    if "open" in f:
                        port = int(f.split("/")[0])
                        ports.append((h,port))

    print(f"[+] Open TCP ports: {ports}")
    return ports


def scan_udp(host="127.0.0.1"):

    if type(host)!= list:
        host = [host]
    ports = []

    for h in host:
        print(f"[+] Running NMAP TCP scan on {h}...")
        result = subprocess.check_output(["nmap", "-sU", "--open", h, "-oG", "-"]).decode()

        for line in result.splitlines():
            if "Ports:" in line:
                fields = line.split("Ports:")[1].split(",")
                for f in fields:
                    if "open" in f:
                        port = int(f.split("/")[0])
                        ports.append((h,port))

    print(f"[+] Open UDP ports: {ports}")
    return ports



# banner
def banner(p):
    host,port = p

    try:
        print(f"[+] Banner grab on {host}:{port}")
        s = socket.socket()
        s.settimeout(15)
        s.connect((host, int(port)))


        data = s.recv(1024)

        print("[Banner]", data.decode(errors="ignore"))
        s.close()
    except Exception as e:
        print("[!] No banner or service refused:", e)


# enum
def enum(p, wordlist):

    host,port = p
    url = f"http://{host}:{port}"
    print(f"[+] Running Gobuster on {url}")

    try:
        subprocess.call(["gobuster", "dir", "-u", url, "-w", wordlist])
    except:
        print("[!] Gobuster not installed or failed")
