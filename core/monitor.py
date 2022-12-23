import os, sys, time, threading

from .utilities.pps import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        # p = PPS()
        # threading.Thread(target=p.run, args=()).start()
        # while True:
        #     print("\r{}".format(p.pps), end="")
        #     time.sleep(1)
        pass