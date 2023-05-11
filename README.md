## Network Connection Monitor

This application monitors network connections and checks for any connected IP addresses that are on a list of malicious IPs or domain addresses. The application consists of two Python scripts, 'app.py' and 'ip_checker.py'.

## Features 

- Retrieves and displays network connections (TCP and UDP) with connection information.
- Monitors connections and alerts if any connected IP addresses are in the list of malicious IPs or domain addresses.
- Resolves domain names to IP addresses.
- Provides process information (PID and process name) for the connections.

## Requirements

- Python 3.x
- psutil (pip install psutil)

## Usage

- Use the text file ips.txt in the same directory as the scripts. Add malicious IP addresses or domain addresses, each on a new line.
- Run app.py to start monitoring network connections. This script will launch ip_checker.py in a separate shell.
- Observe the network connections and alerts for any connected IP addresses that are in the list of malicious IPs or domain addresses.

## app.py

app.py is responsible for:
- Retrieving network connections using the psutil library.
- Displaying network connections and their information, including PID, protocol, local IP, local port, remote IP, remote port, and status.
- Continuously updating and displaying network connections every 3 seconds.

## ip_checker.py

ip_checker.py is responsible for:
- Reading IP address entries from the ips.txt file every 3 seconds.
- Resolving domain names to IP addresses.
- Checking active IP connections against the IP list.
- Displaying alerts if any connected IP addresses match those in the list of malicious IPs or domain addresses, along with connection   information such as protocol, domain, PID, process name, and time.

### Optional 

Use ips.txt to add IP addresses or domains, the script will resolve domain names to IPs. You can add entries to the list and hit save while the program is running and it will incorporate the updates to the list after 3 seconds. 
You can change the refresh rate for app.py and ip_checker.py to be more or less than 3 seconds. 

## See also

ips.txt was composed from this list https://www.maxmind.com/en/high-risk-ip-sample-list
