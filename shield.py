import sys
from core.monitor import *


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print(f"[ x ] Error, Invalid argument provided\r\nUsage: {sys.argv[0]} <interface>")
    exit()

max_pps = 0
c = 0
for arg in sys.argv:
    if arg == "-mp": max_pps = sys.argv[c+1]
    c += 1

CyberShield(sys.argv[1], max_pps)
