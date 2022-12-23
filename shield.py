import os, sys, time

from core.monitor import *
from core.utilities.pps import *

CyberShield()
while True:
    print("\r", end="")
    p = PPS("eth0")
    print("    ", end="\r")
    print(p.pps, end="")