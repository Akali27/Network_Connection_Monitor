## README 


## Description

This application serves as a defensive tool on Windows. It will show the user a list of system port and IP connections and update that list every 5 seconds. Additionally, it will also monitor the connections to check if any domains are on the user's created list of bad IPs. If so, the tool will warn the user in the shell to let them know they're connected to a malicious domain. 

### Built with

- Python 3.11.3 

### Prerequisites

pip install psutil, this is used to monitor system resources including network connections. 

### Install 

Run app.py from terminal. It will automatically launch a second shell, ip_checker.py, while the app.py shell will display network connections and update the list every 5 seconds. ip_checker.py will update every 5 seconds and it will warn the user when there is an active a connection to a domain from the list at ips.txt 

### Configure

Use ips.txt to add to the list. 
You can add IP addresses or domains, the script will resolve domain names to IPs. 

### Usage

This is useful defensive tool. You will be able to see your port connections with the internet and you will also see what processes are prompting the connection. 


### See also

ips.txt was composed from this list https://www.maxmind.com/en/high-risk-ip-sample-list