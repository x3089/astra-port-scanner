import socket
import threading
import argparse

# ASCII Banner
def print_banner():
    print("""
    █████╗ ███████╗████████╗██████╗  █████╗ 
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
    ███████║███████╗   ██║   ██████╔╝███████║
    ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║
    ██║  ██║███████║   ██║   ██║  ██║██║  ██║
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                         
    ASTRA Ethical Port Scanner (EPS v1.0)
    ======================================
    """)

# Function to scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                print(f"[+] Port {port} is open on {ip}")
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

# Main function to handle input and threading
def main():
    parser = argparse.ArgumentParser(description="ASTRA Ethical Port Scanner")
    parser.add_argument("-t", "--target", type=str, required=True, help="Target IP address or domain")
    parser.add_argument("-p", "--ports", type=str, default="1-1024", help="Port range to scan (e.g., 1-65535)")
    parser.add_argument("-o", "--output", type=str, help="File to save scan results")
    args = parser.parse_args()

    # Parse target and port range
    target = args.target
    port_range = args.ports.split("-")
    start_port, end_port = int(port_range[0]), int(port_range[1])

    print(f"[+] Scanning {target} from port {start_port} to {end_port}...")

    # List to hold threads
    threads = []
    results = []

    # Perform scanning
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Save results if output file is provided
    if args.output:
        with open(args.output, "w") as f:
            f.write("ASTRA Port Scanner Results:\n")
            f.write(f"Target: {target}\n")
            f.write(f"Ports Scanned: {start_port}-{end_port}\n")
        print(f"[+] Results saved to {args.output}")

if __name__ == "__main__":
    print_banner()
    print("[!] Use this tool only on networks you own or have explicit permission to test.")
    print("[!] This tool is free to use for ethical purposes. The author is not responsible for any misuse.")
    confirm = input("Do you confirm you have permission? (yes/no): ").strip().lower()
    if confirm == "yes":
        main()
    else:
        print("[!] Exiting. Unauthorized use is prohibited.")
