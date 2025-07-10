import nmap
import sys
from greeting import opening
from scanner import scan

target = sys.argv[1]

opening()

scan(target)
