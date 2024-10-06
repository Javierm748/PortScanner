import socket
from concurrent.futures import ThreadPoolExecutor
import sys
import time

# Function to scan a single port on the target IP address
def scan_port(ip, port):
    """
    Scans a single port to check if it is open or closed.
    
    Args:
        ip (str): The IP address to scan.
        port (int): The port number to check.
    """
    try:
        # Create a new socket using IPv4 and TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the socket
            result = s.connect_ex((ip, port))  # Try to connect to the port
            
            if result == 0:
                # Port is open
                return (port, True)
            else:
                # Port is closed
                return (port, False)
    except socket.error as e:
        # Handle socket errors (e.g., invalid IP)
        print(f"Socket error while scanning port {port}: {e}")
        return (port, False)

# Function to display progress while scanning
def print_progress(current, total):
    """
    Prints the progress of the scan.
    
    Args:
        current (int): The current port being scanned.
        total (int): The total number of ports to scan.
    """
    percent = (current / total) * 100
    bar_length = 40  # Length of the progress bar
    block = int(bar_length * percent / 100)
    progress_bar = f"\r[{'#' * block}{'-' * (bar_length - block)}] {percent:.2f}%"
    sys.stdout.write(progress_bar)
    sys.stdout.flush()

# Main function to scan a range of ports
def port_scanner(ip, start_port, end_port):
    """
    Scans a range of ports on the target IP address.
    
    Args:
        ip (str): The IP address to scan.
        start_port (int): The starting port number.
        end_port (int): The ending port number.
    """
    open_ports = []  # List to store open ports
    total_ports = end_port - start_port + 1  # Total number of ports to scan
    
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    
    # Create a ThreadPoolExecutor for concurrent scanning
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        
        for i, future in enumerate(futures):
            port, is_open = future.result()  # Get the result of the future
            if is_open:
                open_ports.append(port)  # Add to the list of open ports
                print(f"\nPort {port} is open")
            else:
                print(f"\nPort {port} is closed")
            
            # Update progress
            print_progress(i + 1, total_ports)  # Update progress bar
            
    print("\nScan complete.")
    print(f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")


# Entry point of the program
if __name__ == "__main__":
    # Get user input for IP address and port range
    try:
        target_ip = input("Enter the IP address to scan: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        
        # Validate port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Port numbers must be between 1 and 65535 and starting port must be less than or equal to ending port.")
        
        # Start port scanning
        port_scanner(target_ip, start_port, end_port)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


