import os, sys, time, threading

from .utilities.tools.pps import *
from .fx.design import *
from .utilities.config.config import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        #grab config information
        #display os, hardware, connection, motd and other information that doesn't update

        # LATER THING: start socket server here
        self.sfx = ShieldFX()
        self.cfg = Config()
        
        print("\033[8;{};{}t".format(self.cfg.term.size[0], self.cfg.term.size[1]), end="")
        print(self.sfx.render_ui(), end="")
        self.start_listener()

    def start_listener(self) -> None:
        # grab config information incase its needed for future features
        self.pps = PPS("eth0")
        while True:
            print("\033[{0};{1}f{2}".format(self.cfg.ppscfg.pps_p[0], self.cfg.ppscfg.pps_p[1], self.pps.updatePPS()), end="")