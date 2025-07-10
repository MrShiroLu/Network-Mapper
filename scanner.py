import nmap
import time
import sys

def scan(target):
    scanner = nmap.PortScanner()

    start_time = time.time()

    scanner.scan(target)

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")

        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")
            ports = scanner[host][protocol].keys()

            for port in ports:
                print(f"Port: {port}\tState: {scanner[host][protocol][port]["state"]}\t Service: {scanner[host][protocol][port]["name"]/scanner[host][protocol][port]["product"]}") 

    end_time = time.time()
    total_time = int(end_time - start_time)
    print(f"\nTotal time: {total_time} seconds!")
    print("-"*80)