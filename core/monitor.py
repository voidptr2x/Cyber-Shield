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
        if self.cfg.hdw.display == True:
            if self.cfg.hdw.cpu_name_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.cpu_name_p[0]};{self.cfg.hdw.cpu_name_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"CPU: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.cpu_name, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.cpu_cores_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.cpu_cores_p[0]};{self.cfg.hdw.cpu_cores_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"CPU Cores: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.cpu_cores, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.cpu_freq_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.cpu_freq_p[0]};{self.cfg.hdw.cpu_freq_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"CPU Frequency: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.cpu_freq, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.cpu_temp_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.cpu_temp_p[0]};{self.cfg.hdw.cpu_temp_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"CPU Temperature: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.cpu_temp, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.cpu_usage_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.cpu_usage_p[0]};{self.cfg.hdw.cpu_usage_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"CPU Usage: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.cpu_usage, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_usage_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_usage_p[0]};{self.cfg.hdw.ram_usage_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Usage: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_usage, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_total_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_total_p[0]};{self.cfg.hdw.ram_total_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Total: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_total, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_free_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_free_p[0]};{self.cfg.hdw.ram_free_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Free: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_free, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_used_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_used_p[0]};{self.cfg.hdw.ram_used_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Used: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_used, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_available_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_available_p[0]};{self.cfg.hdw.ram_available_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Available: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_available, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.ram_percent_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.ram_percent_p[0]};{self.cfg.hdw.ram_percent_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"RAM Percent: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.ram_percent, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.swap_total_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.swap_total_p[0]};{self.cfg.hdw.swap_total_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"Swap Total: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.swap_total, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.swap_free_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.swap_free_p[0]};{self.cfg.hdw.swap_free_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"Swap Free: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.swap_free, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.swap_used_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.swap_used_p[0]};{self.cfg.hdw.swap_used_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"Swap Used: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.swap_used, end="")
                print("\x1b[0m", end="")
            if self.cfg.hdw.swap_percent_p != [0, 0]:
                print(f"\x1b[{self.cfg.hdw.swap_percent_p[0]};{self.cfg.hdw.swap_percent_p[1]}f\x1b[38;2;{self.cfg.hdw.labels_c[0]};{self.cfg.hdw.labels_c[1]};{self.cfg.hdw.labels_c[2]}m", end="")
                print(f"Swap Percent: ", end="")
                print(f"\x1b[38;2;{self.cfg.hdw.value_c[0]};{self.cfg.hdw.value_c[1]};{self.cfg.hdw.value_c[2]}m", end="")
                print(self.os.swap_percent, end="")
                print("\x1b[0m", end="")
 
    def start_listener(self) -> None:
        self.pps = PPS("eth0")

        while True:
            print(f"\x1b[{self.cfg.ppscfg.pps_p[0]};{self.cfg.ppscfg.pps_p[1]}f", end=" ")
            print(f"PPS: {self.pps.updatePPS()}")