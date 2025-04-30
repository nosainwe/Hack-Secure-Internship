import socket
import sys
from datetime import datetime

def scan_ports(target, start_port, end_port):
    try:
        # Validate IP
        socket.inet_aton(target)
    except socket.error:
        print("Invalid IP address")
        return

    # Validate port range
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print("Invalid port range. Ports must be between 1 and 65535")
        return

    print(f"Scanning {target} from port {start_port} to {end_port}...")
    start_time = datetime.now()

    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    print(f"Scan completed in {datetime.now() - start_time}")
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <IP> <start_port> <end_port>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    except ValueError:
        print("Ports must be integers")
        sys.exit(1)

    scan_ports(target, start_port, end_port)
