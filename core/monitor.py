import os, sys, time, threading

from .utilities.tools.pps import *
from .fx.design import *
from .utilities.config.config import *
from .utilities.os import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        # grab config information
        # display os, hardware, connection, motd and other information that doesn't update

        # LATER THING: start socket server here
        self.sfx = ShieldFX()
        self.cfg = Config()
        self.os = OS()
        
        print("\033[?25l") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end=" ") # Set Terminal Size
        print("\x1b[0;0f")
        print(self.sfx.render_ui(), end="") # Set UI

        self.start_listener()

    def start_listener(self) -> dNone:
        self.pps = PPS("eth0")

        if self.cfg.os.display == True:
            print(f"\x1b[{self.cfg.os.os_name_p[0]};{self.cfg.os.os_name_p[1]}f", end=" ")
            print(f"OS: {self.os.os_name}")

        while True:
            print(f"\x1b[{self.cfg.ppscfg.pps_p[0]};{self.cfg.ppscfg.pps_p[1]}f", end=" ")
            print(f"PPS: {self.pps.updatePPS()}")