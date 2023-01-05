import os, sys, time

from core.monitor import *

if len(sys.argv) > 1 or len(sys.argv) < 1:
    print(f"[ x ] Error, Invalid argument provided\r\nUsage: {sys.argv[0]} <interface>")
    exit()

# Validate interface here
CyberShield(sys.argv[2])