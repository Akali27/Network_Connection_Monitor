# ip_checker.py
import psutil
import time
import socket
from urllib.parse import urlparse

print("This shell will display any connected IP addresses that are on the list of malicious IPs or URL addresses")

#Read IP address entries
def get_ips(file_path):
    with open(file_path, 'r') as file:
        entries = [line.strip() for line in file.readlines()]
    return entries

#Resolve domain names and URLs to IP addresses
def resolve_domains(entries):
    ips = set()
    for entry in entries:
        try:
            # If entry is a URL, extract the domain and resolve to IP
            if entry.startswith("https" or "http"):
                domain = urlparse(entry).hostname
            else:
                domain = entry

            ip = socket.gethostbyname(domain)
            ips.add(ip)
        except socket.gaierror:
            ips.add(entry) # If entry is an IP address, include it 
    return ips

#Check active IP connections against IP list
def check_ips(connections, ips):
    for conn in connections:
        # Check for TCP and UDP connections from remote addresses
        if conn.status != 'NONE' and (conn.type == 1 or conn.type == 2) and conn.raddr:  
            if conn.raddr.ip in ips:
                protocol = "TCP" if conn.type == 1 else "UDP"
                print(f"Matching IP found ({protocol}): {conn.raddr.ip}")

if __name__ == "__main__":
    # Read frome file and resolve to IP addresses
    entries = get_ips('ips.txt')
    ips = resolve_domains(entries)

    while True:
        connections = psutil.net_connections(kind='inet')
        check_ips(connections, ips)
        time.sleep(5)  # Update every 5 seconds
