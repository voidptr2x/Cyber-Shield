import os, sys, time, threading

from .utilities.tools.pps import *
from .fx.design import *
from .utilities.config.config import *
from .utilities.os import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        self.sfx = ShieldFX()
        self.cfg = Config()
        self.os = OS()
        
        print("\033[?25l") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end=" ") # Set Terminal Size
        print("\x1b[0;0f")
        print(self.sfx.render_ui(), end="") # Set UI

        self.set_info()
        self.start_listener()

    def set_info(self) -> None:
        if self.cfg.os.display == True:
            if self.cfg.os.os_name_p != [0, 0]:
                print(f"\x1b[{self.cfg.os.os_name_p[0]};{self.cfg.os.os_name_p[1]}f\x1b[38;2;{self.cfg.os.labels_c[0]};{self.cfg.os.labels_c[1]};{self.cfg.os.labels_c[2]}m", end="")
                print(f"OS: ", end="")
                print(f"\x1b[38;2;{self.cfg.os.value_c[0]};{self.cfg.os.value_c[1]};{self.cfg.os.value_c[2]}m", end="")
                print(self.os.os_name, end="")

                print(f"\x1b[{self.cfg.os.os_version_p[0]};{self.cfg.os.os_version_p[1]}f\x1b[38;2;{self.cfg.os.labels_c[0]};{self.cfg.os.labels_c[1]};{self.cfg.os.labels_c[2]}m", end="")
                print(f"OS Version: ", end="")
                print(f"\x1b[38;2;{self.cfg.os.value_c[0]};{self.cfg.os.value_c[1]};{self.cfg.os.value_c[2]}m", end="")
                print(self.os.os_version, end="")


                print(f"\x1b[{self.cfg.os.os_kernel_p[0]};{self.cfg.os.os_kernel_p[1]}f\x1b[38;2;{self.cfg.os.labels_c[0]};{self.cfg.os.labels_c[1]};{self.cfg.os.labels_c[2]}m", end="")
                print(f"OS Kernel: ", end="")
                print(f"\x1b[38;2;{self.cfg.os.value_c[0]};{self.cfg.os.value_c[1]};{self.cfg.os.value_c[2]}m", end="")
                print(self.os.os_kernel, end="")


                print("\x1b[0m", end="")

    def start_listener(self) -> None:
        self.pps = PPS("eth0")

        while True:
            print(f"\x1b[{self.cfg.ppscfg.pps_p[0]};{self.cfg.ppscfg.pps_p[1]}f", end=" ")
            print(f"PPS: {self.pps.updatePPS()}")