import os, sys, time, threading

from .tools.pps import *
from .fx.design import *
from .config.config import *
from .tools.os import *
from .tools.hardware import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        self.sfx = ShieldFX()
        self.cfg = Config()
        self.os = OS()
        self.hdw = Hardware()
        self.pps = PPS("eth0")
        
        print("\033[?25l") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end=" ") # Set Terminal Size
        print("\x1b[0;0f")
        print(self.sfx.render_ui(), end="") # Set UI

        self.set_info()
        threading.Thread(target=self.pps.runPPS).start()
        self.start_listener()

    def set_info(self) -> None:
        if self.cfg.os.display:
            if self.cfg.os.os_name_p != [0, 0]:
                # OS Name
                self._placeLabel(self.cfg.os.os_name_p, self.cfg.os.labels_c, "OS: ")
                self._placeValue(self.cfg.os.value_c, self.os.info.os_name)
                # OS Version
                self._placeLabel(self.cfg.os.os_version_p, self.cfg.os.labels_c, "OS Version: ")
                self._placeValue(self.cfg.os.value_c, self.os.info.os_version)
                # OS Kernel
                self._placeLabel(self.cfg.os.os_kernel_p, self.cfg.os.labels_c, "OS Kernel: ")
                self._placeValue(self.cfg.os.value_c, self.os.info.os_kernel)
                # OS Shell
                self._placeLabel(self.cfg.os.shell_p, self.cfg.os.labels_c, "Shell: ")
                self._placeValue(self.cfg.os.value_c, self.os.info.os_current_shell)

        if self.cfg.hdw.display:
            if self.cfg.hdw.cpu_name_p != [0, 0]:
                # CPU Name
                self._placeLabel(self.cfg.hdw.cpu_name_p, self.cfg.hdw.labels_c, "CPU: ")
                self._placeValue(self.cfg.hdw.value_c, self.hdw.info.cpu_name)

    def start_listener(self) -> None:

        while True:
            self._placeLabel(self.cfg.ppscfg.pps_p, self.cfg.ppscfg.pps_label_c, "PPS: ")
            self._placeValue(self.cfg.ppscfg.pps_value_c, str(self.pps.f_pps))
            time.sleep(0.01)
            self._placeValue(self.cfg.ppscfg.pps_value_c, "     ")
    
    def _placeLabel(self, position: list, color: list, text: str) -> None:
        print(f"\x1b[{position[0]};{position[1]}f\x1b[38;2;{color[0]};{color[1]};{color[2]}m", end="")
        print(f"{text}", end="")
        print("\x1b[0m", end="")

    def _placeValue(self, color: list, text: str) -> None:
        print(f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m", end="")
        print(f"{text}", end="")
        print("\x1b[0m", end="")