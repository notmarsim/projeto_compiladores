import subprocess
import socket

# nmap
def scan_tcp(host):
    print(f"[+] Running NMAP TCP scan on {host}...")
    # result = subprocess.check_output(["nmap", "-p-", "--open", host, "-oG", "-"]).decode()

    # ports = []
    # for line in result.splitlines():
    #     if "Ports:" in line:
    #         fields = line.split("Ports:")[1].split(",")
    #         for f in fields:
    #             if "open" in f:
    #                 port = int(f.split("/")[0])
    #                 ports.append(port)

    # print(f"[+] Open TCP ports: {ports}")
    return [80,143]


def scan_udp(host):
    
    # result = subprocess.check_output(["nmap", "-sU", "--open", host, "-oG", "-"]).decode()

    # ports = []
    # for line in result.splitlines():
    #     if "Ports:" in line:
    #         fields = line.split("Ports:")[1].split(",")
    #         for f in fields:
    #             if "open" in f:
    #                 port = int(f.split("/")[0])
    #                 ports.append(port)

    # print(f"[+] Open UDP ports: {ports}")
    return print(f"[+] Running NMAP UDP scan on {host} (may be slow)...")



# banner
def banner(port, host="127.0.0.1"):
    print(f"[+] Banner grab on {host}:{port}")
    # try:
    #     s = socket.socket()
    #     s.settimeout(2)
    #     s.connect((host, int(port)))
    #     s.send(b"HELLO\r\n")
    #     data = s.recv(1024)
    #     print("[Banner]", data.decode(errors="ignore"))
    #     s.close()
    # except Exception as e:
    #     print("[!] No banner or service refused:", e)


# enum
def enum(port, host="127.0.0.1"):
    url = f"http://{host}:{port}"
    print(f"[+] Running Gobuster on {url}")

    # try:
    #     subprocess.call(["gobuster", "dir", "-u", url, "-w", "/usr/share/wordlists/dirb/common.txt"])
    # except:
    #     print("[!] Gobuster not installed or failed")
