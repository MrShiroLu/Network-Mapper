import nmap
import sys
from greeting import opening
from scanner import scan

target = sys.argv[1]

for i in sys.argv:
    if i == "-p":
        target_port = str(sys.argv[sys.argv.index(i) + 1])
        break

opening()

scan(target,target_port)