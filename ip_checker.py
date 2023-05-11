# Import Dependencies
import psutil
import time
import socket
from urllib.parse import urlparse

print("This shell will display any connected IP addresses that are on the list of malicious IPs or domain addresses")

# Read IP address entries every 3 seconds
def get_ips(file_path):
    while True:
        with open(file_path, 'r') as file:
            entries = [line.strip() for line in file.readlines()]
        yield entries
        time.sleep(3)  # Refresh IP list every 3 seconds

# Resolve domain names and IP addresses 
def resolve_domains(entries):
    ip_to_domain = {}
    for entry in entries:
        try:
            # If entry is a URL, extract the domain and resolve to IP
            if entry.startswith("https" or "http"):
                domain = urlparse(entry).hostname
            else:
                domain = entry

            ip = socket.gethostbyname(domain)
            ip_to_domain[ip] = domain #Get the domain name from IP
        except socket.gaierror:
            ip_to_domain[entry] = entry  # If entry is an IP address, include it
    return ip_to_domain

# Check active IP connections against IP list
def check_ips(connections, ip_to_domain):
    for conn in connections:
        # Check for TCP and UDP connections from remote addresses
        if conn.status != 'NONE' and (conn.type == 1 or conn.type == 2) and conn.raddr:
            ip = conn.raddr.ip
            if ip in ip_to_domain:
                protocol = "TCP" if conn.type == 1 else "UDP"
                domain = ip_to_domain[ip] #Get domain address
                try:
                    process = psutil.Process(conn.pid) #Get process id that's connected to IP
                    timestamp = time.strftime('%H:%M:%S', time.localtime(process.create_time())) #Get time connection happened
                    process_name = process.name() #Get process name that's connected to the IP
                except (psutil.NoSuchProcess, AttributeError):
                    timestamp = "Unknown" #Replace timestamp with unknown if time isn't received 
                    process_name = "Unknown" #Replace process name with unknown if process name isn't received 
                print(f"Matching IP found ({protocol}): {ip}, Domain: {domain}, PID: {conn.pid}, Process Name: {process_name}, Time: {timestamp}")

if __name__ == "__main__":
    ip_list = get_ips('ips.txt')

    while True:
        entries = next(ip_list)
        ip_to_domain = resolve_domains(entries)
        connections = psutil.net_connections(kind='inet')
        check_ips(connections, ip_to_domain)
        time.sleep(3)  # Update every 3 seconds
