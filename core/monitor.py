import os, sys, time, threading

from .fx.design import *
from .config.config import *

from .tools.os import *
from .tools.hardware import *
from .tools.connection import *

from .utilities.term_control import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self, interface) -> None:
        self.sfx, self.cfg, self.os, self.hdw, self.pps = [ShieldFX(), Config(), OS(), Hardware(), Connection(interface)]

        """
        Pull all interfaces to check if there more than one interface. if so, request user for the interface to use
        """
        
        print("\033[?25l\x1b[37m", end="") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end="") # Set Terminal Size
        print("\x1b[0;0f", end="")
        print(self.sfx.render_ui(), end="") # Set UI

        self.set_info()
        threading.Thread(target=self.pps.runPPS).start()
        self.start_listener()

    def set_info(self) -> None:
        if self.cfg.os.display == True:
            if self.cfg.os.os_name_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_name_p, self.cfg.os.labels_c, "OS: ", self.cfg.os.value_c, self.os.info.os_name)
            if self.cfg.os.os_version_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_version_p, self.cfg.os.labels_c, "OS Version: ", self.cfg.os.value_c, self.os.info.os_version)
            if self.cfg.os.os_kernel_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_kernel_p, self.cfg.os.labels_c, "OS Kernel: ", self.cfg.os.value_c, self.os.info.os_kernel)

        if self.cfg.hdw.display == True:
            if self.cfg.hdw.cpu_name_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.cpu_name_p, self.cfg.hdw.labels_c, "CPU Name: ", self.cfg.hdw.value_c, self.hdw.info.cpu_name)
            if self.cfg.hdw.cpu_name_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.cpu_cores_p, self.cfg.hdw.labels_c, "CPU Cores: ", self.cfg.hdw.value_c, self.hdw.info.cpu_cores)

    def start_listener(self) -> None:
        while True:
            TerminalControl.placeTextAlt(self.cfg.conn.pps_p, "               ")
            TerminalControl.placeText(self.cfg.conn.pps_p, self.cfg.conn.labels_c, "PPS: ", self.cfg.conn.value_c, self.pps.f_pps)
            
            TerminalControl.placeTextAlt(self.cfg.hdw.cpu_usage_p, "               ")
            TerminalControl.placeText(self.cfg.hdw.cpu_usage_p, self.cfg.hdw.labels_c, "CPU Usage: ", self.cfg.hdw.value_c, self.hdw.info.cpu_usage)
            time.sleep(1)