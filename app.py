#app.py
import psutil
import time
import subprocess

#Retrieve network connections using psutil
def get_connections():
    connections = psutil.net_connections(kind='inet')
    return connections

#Print all network connections
def print_connections(connections):
    print("PID    Protocol    Local IP                 Local Port                Remote IP           Remote Port        Status")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    # Iterate through the connections and print each connection's information
    for conn in connections:
        if conn.status != 'NONE':
            protocol = "TCP" if conn.type == 1 else "UDP" if conn.type == 2 else "OTHER"
            loadr1 = conn.laddr.ip
            loadr2 = conn.laddr.port
            readr1 = f"{conn.raddr.ip}" if conn.raddr else ""
            readr2 = f"{conn.raddr.port}" if conn.raddr else ""
            print(f"{conn.pid:<6} {protocol:<9} {loadr1:<25} {loadr2:<25} {readr1:<20} {readr2:<20} {conn.status}")
    print("\n")

if __name__ == "__main__":
    # Launch ip_checker.py in a separate shell
    checker_script = 'ip_checker.py'
    subprocess.Popen(['python', checker_script], creationflags=subprocess.CREATE_NEW_CONSOLE)

    try:
        # Continuously update and display the network connections
        while True:
            connections = get_connections()
            print_connections(connections)
            time.sleep(3)  # Update every 3 seconds
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to exit the script
        print("Exiting...")
