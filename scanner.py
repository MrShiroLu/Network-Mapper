import nmap
import time
import sys

def scan(target,target_port):
    scanner = nmap.PortScanner()

    start_time = time.time()

    scanner.scan(target,target_port, arguments='-T4 -Pn')

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")

        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")
            ports = scanner[host][protocol].keys()

            for port in ports:
                print(f"Port: {port}\tState: {scanner[host][protocol][port]["state"]}\tService: {scanner[host][protocol][port]["name"]}\t Version: {scanner[host][protocol][port]["version"]}") 

    end_time = time.time()
    total_time = int(end_time - start_time)
    print(f"\nTotal time: {total_time} seconds!")
    print("-"*80)