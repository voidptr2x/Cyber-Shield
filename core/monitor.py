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
        
        print("\033[?25l\x1b[37m") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end=" ") # Set Terminal Size
        print("\x1b[0;0f")
        print(self.sfx.render_ui(), end="") # Set UI

        self.set_info()
        threading.Thread(target=self.pps.runPPS).start()
        self.start_listener()

    def set_info(self) -> None:
        if self.cfg.os.display == True:
            if self.cfg.os.os_name_p != [0, 0]:
                TerminalControl.placeText(self.cfg.os.os_name_p, self.cfg.os.labels_c, "OS: ", self.cfg.os.value_c, self.os.info.os_name)
                TerminalControl.placeText(self.cfg.os.os_version_p, self.cfg.os.labels_c, "OS Version: ", self.cfg.os.value_c, self.os.info.os_version)
                TerminalControl.placeText(self.cfg.os.os_kernel_p, self.cfg.os.labels_c, "OS Kernel: ", self.cfg.os.value_c, self.os.info.os_kernel)

        if self.cfg.hdw.display == True:
            if self.cfg.hdw.cpu_name_p != [0, 0]:
                TerminalControl.placeText(self.cfg.hdw.cpu_name_p, self.cfg.hdw.labels_c, "CPU Name: ", self.cfg.hdw.value_c, self.hdw.info.cpu_name)

            # if self.cfg.hdw.cpu_cores_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.cpu_cores_p[0]};{self.cfg.hdw.cpu_cores_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"CPU Cores: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.hdw, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.cpu_count_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.cpu_count_p[0]};{self.cfg.hdw.cpu_count_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"CPU Count: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.cpu_count_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.cpu_usage_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.cpu_usage_p[0]};{self.cfg.hdw.cpu_usage_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"CPU Usage: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.cpu_usage_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.memory_name_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.memory_name_p[0]};{self.cfg.hdw.memory_name_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"RAM Name: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.memory_name_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.memory_capacity_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.memory_capacity_p[0]};{self.cfg.hdw.memory_capacity_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"RAM Capacity: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.memory_capacity_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.memory_used_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.memory_used_p[0]};{self.cfg.hdw.memory_used_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"RAM Used: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.memory_used_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.memory_free_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.memory_free_p[0]};{self.cfg.hdw.memory_free_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"RAM Free: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.memory_free_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.hdd_name_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.hdd_name_p[0]};{self.cfg.hdw.hdd_name_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"HDD Name: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.hdd_name_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.hdd_capacity_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.hdd_capacity_p[0]};{self.cfg.hdw.hdd_capacity_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"HDD Capacity: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.hdd_capacity_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.hdd_usage_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.hdd_usage_p[0]};{self.cfg.hdw.hdd_usage_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"HDD Usage: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.hdd_usage_p, end="")
            #     print("\x1b[0m", end="")
            # if self.cfg.hdw.hdd_free_p != [0, 0]:
            #     print(f"\x1b[{self.cfg.hdw.hdd_free_p[0]};{self.cfg.hdw.hdd_free_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
            #     print(f"HDD Free: ", end="")
            #     print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
            #     print(self.cfg.hdw.hdd_free_p, end="")
            #     print("\x1b[0m", end="")
 
    def start_listener(self) -> None:
        while True:
            TerminalControl.placeTextAlt(self.cfg.conn.pps_p, "               ")
            TerminalControl.placeText(self.cfg.conn.pps_p, self.cfg.conn.labels_c, "PPS: ", self.cfg.conn.value_c, self.pps.f_pps)
            
            time.sleep(1)