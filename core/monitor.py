import os, sys, time, threading

from .fx.design import *
from .fx.graph import *

from .config.config import *

from .tools.os import *
from .tools.hardware import *
from .tools.connection import *

from .utilities.term_control import *

class CyberShield():
    current_interface: str
    interfaces: list
    max_pps: int
    
    def __init__(self, interface, mp: int) -> None:
        self.sfx, self.cfg, self.os, self.hdw, self.pps, self.graph, self.nload, self.max_pps = [ShieldFX(), Config(), OS(), Hardware(), Connection(interface), Graph(23, 65), Nload(), mp]

        threading.Thread(target=self.nload.runNload).start()
        g = threading.Thread(target=self.pps.get_speed).start()
        """
        Pull all interfaces to check if there more than one interface. if so, request user for the interface to use
        """
        print(chr(27) + "[2J", end="") # Clear Screen
        print("\033[?25l\x1b[37m", end="") # Hide Cursor
        print(f"\x1b[8;{self.cfg.term.size[0]};{self.cfg.term.size[1]}t", end="") # Set Terminal Size
        print("\x1b[0;0f", end="")
        print(self.sfx.render_ui(), end="") # Set UI
        TerminalControl.move_cursor([11, 37])
        TerminalControl.listText_c([11, 37], [255, 255, 255], self.graph.get_graph_layout())
        self.hdw.updateInfo()

        self.set_info()
        threading.Thread(target=self.pps.runPPS).start()
        self.start_listener()

    def set_info(self) -> None:
        if self.cfg.os.display == True:
            if self.cfg.os.os_name_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_name_p, self.cfg.os.labels_c, "OS: ", self.cfg.os.value_c, self.os.info._name)
            if self.cfg.os.os_version_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_version_p, self.cfg.os.labels_c, "OS Version: ", self.cfg.os.value_c, self.os.info._version)
            if self.cfg.os.os_kernel_p != [0, 0]: TerminalControl.placeText(self.cfg.os.os_kernel_p, self.cfg.os.labels_c, "OS Kernel: ", self.cfg.os.value_c, self.os.info._kernel)
            if self.cfg.os.shell_p != [0, 0]: TerminalControl.placeText(self.cfg.os.shell_p, self.cfg.os.labels_c, "Shell: ", self.cfg.os.value_c, self.os.info._shell)

        if self.cfg.hdw.display == True:
            if self.cfg.hdw.cpu_name_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.cpu_name_p, self.cfg.hdw.labels_c, "CPU Name: ", self.cfg.hdw.value_c, self.hdw.info.cpu_name[0:20])
            if self.cfg.hdw.cpu_cores_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.cpu_cores_p, self.cfg.hdw.labels_c, "CPU Cores: ", self.cfg.hdw.value_c, self.hdw.info.cpu_cores)

            if self.cfg.hdw.memory_capacity_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.memory_capacity_p, self.cfg.hdw.labels_c, "Memory Capacity: ", self.cfg.hdw.value_c, f"{self.hdw.info.memory_capacity} GB")
            if self.cfg.hdw.memory_used_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.memory_used_p, self.cfg.hdw.labels_c, "Memory Used: ", self.cfg.hdw.value_c, f"{self.hdw.info.memory_used} GB")
            if self.cfg.hdw.memory_free_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.memory_free_p, self.cfg.hdw.labels_c, "Memory Free: ", self.cfg.hdw.value_c, f"{self.hdw.info.memory_free} GB")
            if self.cfg.hdw.memory_usage_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.memory_usage_p, self.cfg.hdw.labels_c, "Memory Usage: ", self.cfg.hdw.value_c, f"{self.hdw.info.memory_used}/{self.hdw.info.memory_capacity} GB")

            if self.cfg.hdw.hdd_capacity_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.hdd_capacity_p, self.cfg.hdw.labels_c, "HDD Capacity: ", self.cfg.hdw.value_c, f"{self.hdw.info.hdd_capacity} GB")
            if self.cfg.hdw.hdd_used_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.hdd_used_p, self.cfg.hdw.labels_c, "HDD Used: ", self.cfg.hdw.value_c, f"{self.hdw.info.hdd_used} GB")
            if self.cfg.hdw.hdd_free_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.hdd_free_p, self.cfg.hdw.labels_c, "HDD Free: ", self.cfg.hdw.value_c, f"{self.hdw.info.hdd_free} GB")
            if self.cfg.hdw.hdd_usage_p != [0, 0]: TerminalControl.placeText(self.cfg.hdw.hdd_usage_p, self.cfg.hdw.labels_c, "HDD Usage: ", self.cfg.hdw.value_c, f"{self.hdw.info.hdd_used}/{self.hdw.info.hdd_capacity} GB")

        if self.cfg.conn.display:
            if self.cfg.conn.ip != [0, 0]: TerminalControl.placeText(self.cfg.conn.ip, self.cfg.conn.labels_c, "System IP: ", self.cfg.conn.value_c, self.pps.get_sys_ip())

    def start_listener(self) -> None:
        self.hdw.updateInfo()
        while True:
            if self.max_pps > self.pps.f_pps and self.max_pps != 0:
                print("\033]0;Cyber Shield v3.00 | Status: Offline....\007", end="")
            else: print("\033]0;Cyber Shield v3.00 | Status: Online....\007", end="")
            if self.cfg.conn.nload_stats_p != [0, 0]: TerminalControl.listText_c(self.cfg.conn.nload_stats_p, self.cfg.conn.value_c, self.nload.get_raw_text())
            if self.pps.upload != "": 
                if self.cfg.conn.upload_speed_p != [0, 0]: TerminalControl.placeText(self.cfg.conn.upload_speed_p, self.cfg.conn.labels_c, "Upload: ", self.cfg.conn.value_c, self.pps.upload)
                if self.cfg.conn.download_speed_p != [0, 0]: TerminalControl.placeText(self.cfg.conn.download_speed_p, self.cfg.conn.labels_c, "Download: ", self.cfg.conn.value_c, self.pps.download)
            else:
                if self.cfg.conn.upload_speed_p != [0, 0]: TerminalControl.placeText(self.cfg.conn.upload_speed_p, self.cfg.conn.labels_c, "Upload: ", self.cfg.conn.value_c, "N/A")
                if self.cfg.conn.download_speed_p != [0, 0]: TerminalControl.placeText(self.cfg.conn.download_speed_p, self.cfg.conn.labels_c, "Download: ", self.cfg.conn.value_c, "N/A")

            self.graph.append_to_graph(self.pps.f_pps)
            TerminalControl.listText(self.cfg.graph.graph_p, self.graph.render_graph().replace("#", TerminalControl.ansiColor(self.cfg.graph.data_c) + "#\x1b[0m",).replace(".", "\x1b[37m.\x1b[0m"))

            TerminalControl.place_text(self.cfg.conn.pps_p, "               ")
            TerminalControl.place_text(self.cfg.hdw.cpu_usage_p, "                      ")
            TerminalControl.placeText(self.cfg.conn.pps_p, self.cfg.conn.labels_c, "PPS: ", self.cfg.conn.value_c, self.pps.f_pps)
            TerminalControl.placeText(self.cfg.hdw.cpu_usage_p, self.cfg.hdw.labels_c, "CPU Usage: ", self.cfg.hdw.value_c, self.hdw.info.cpu_usage)
            time.sleep(1)