## README 


## Description

This application serves as a defensive tool on Windows. It will show the user a list of active connections and update the list every 3 seconds. It will display the PID of the local process initiating the connection, type of connection (tcp/udp), local IP and port, remote IP and port, and connection status (ESTABLISHED, LISTEN, SYN_RECV, etc...). 

Additionally, it will also monitor the connections in a separate shell to check if the system is connecting to any matches from the created list of bad IPs and domains. If so, the tool will warn the user to let them know they're connected to a malicious domain. It will list the IP address, domain name, PID, process name, and time connection happened. 

### Built with

- Python 3.11.3 

### Prerequisites

pip install psutil, this is used to monitor system resources including network connections. 

### Operation 

Run app.py from terminal. It will automatically launch a second shell, ip_checker.py, while the app.py shell will display network connections and update the list every 3 seconds. ip_checker.py will update every 3 seconds and it will warn the user when there is an active connection to an entry from the list at ips.txt 

### Optional 

Use ips.txt to add to the list. You can add IP addresses or domains, the script will resolve domain names to IPs. You can add entries to the list and hit save while the program is running and it will incorporate the updates to the list after 3 seconds. 
You can change the refresh rate for app.py and ip_checker.py to be more or less than 3 seconds. 

### Usage

This is a useful defensive tool. You will be able to see your port connections with the internet and you will also see what processes are prompting the connection. 


### See also

ips.txt was composed from this list https://www.maxmind.com/en/high-risk-ip-sample-list
