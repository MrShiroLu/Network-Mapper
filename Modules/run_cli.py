import sys
from greeting import opening
from scanner import scan

target = sys.argv[1] # Target IP or hostname

arguments = "-T4 -Pn" # Default arguments
target_port = "1-65535"  # Default to scan all ports

for i in sys.argv:
    if i == "-p":
        target_port = str(sys.argv[sys.argv.index(i) + 1])
        print(f"Using ports: {target_port}")
    elif i == "-a":
        arguments = ""
        for arg in sys.argv[sys.argv.index(i) + 1:]:
            arguments += str(sys.argv[sys.argv.index(arg)]) + " "
        print(f"Using arguments: {arguments} ")

opening()
scan(target, target_port,arguments)