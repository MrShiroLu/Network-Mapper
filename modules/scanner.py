import nmap
import time

def scan(target, target_port,arguments):
    scanner = nmap.PortScanner()
    results = []

    start_time = time.time()

    scanner.scan(target, target_port, arguments)
    print(f"Using arguments: {arguments} ")

    for host in scanner.all_hosts():
        results.append(f"Host: {host}")
        results.append(f"State: {scanner[host].state()}")

        for protocol in scanner[host].all_protocols():
            results.append(f"Protocol: {protocol}")
            ports = scanner[host][protocol].keys()

            for port in ports:
                port_info = f"Port: {port}\tState: {scanner[host][protocol][port]['state']}\tService: {scanner[host][protocol][port]['name']}\t Version: {scanner[host][protocol][port]['version']}"
                results.append(port_info)

    end_time = time.time()
    total_time = format((end_time - start_time), '.2f')
    
    results.append(f"\nTotal time: {total_time} seconds!")
    results.append("="*80)
    
    # Printing for tkinter
    for result in results:
        print(result)
    
    return results