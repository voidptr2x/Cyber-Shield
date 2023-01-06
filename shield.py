import sys
from core.monitor import *


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print(f"[ x ] Error, Invalid argument provided\r\nUsage: {sys.argv[0]} <interface>")
    exit()

CyberShield(sys.argv[1])
