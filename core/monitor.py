import os, sys, time, threading

from .utilities.pps import *

class CyberShield():
    def __init__(self) -> None:
        p = PPS()
        threading.Thread(target=p.run, args=()).start()
        while True:
            print("\r{}".format(p.pps), end="")
            time.sleep(1)
