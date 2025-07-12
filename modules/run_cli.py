import sys
from greeting import opening
from scanner import scan

target = sys.argv[1]
arguments = "-T4 -Pn"

for i in sys.argv:
    if i == "-p":
        target_port = str(sys.argv[sys.argv.index(i) + 1])
    elif i == "-a":
        arguments = ""
        for arg in sys.argv[sys.argv.index(i) + 1:]:
            arguments += str(sys.argv[sys.argv.index(arg)]) + " "
        print(f"Using arguments: {arguments} ")

opening()
scan(target, target_port,arguments)