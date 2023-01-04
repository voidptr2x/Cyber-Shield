import os, sys, time, subprocess

class Connection():
    f_pps: int
    def __init__(self, iface: str) -> None:
        self.interface = iface
        self.f_pps = 0

    """
    Run this in a thread then use the 'pps' objects to get the updated PPS
    """
    def runPPS(self):
        while True:
            rx, tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/tx_packets"))]
            # print(f"Old: {rx} | {tx}")
            time.sleep(1)
            new_rx, new_tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/tx_packets"))]
            # print(f"New: {new_rx} | {new_tx}")
            self.f_pps = 0
            self.f_pps = (tx - new_tx) - (rx - new_rx)