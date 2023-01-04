import sys, os, time, subprocess
display_pps = ""

def pps(iface):
    rx, tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{iface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{iface}/statistics/tx_packets"))]
    # print(f"Old: {rx} | {tx}")
    time.sleep(1)
    new_rx, new_tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{iface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{iface}/statistics/tx_packets"))]
    # print(f"New: {new_rx} | {new_tx}")
    return (tx - new_tx) - (rx - new_rx)

class PPS():
    f_pps: int
    def __init__(self, iface: str) -> None:
        self.interface = iface
        self.f_pps = 0

    def runPPS(self):
        while True:
            rx, tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/tx_packets"))]
            # print(f"Old: {rx} | {tx}")
            time.sleep(1)
            new_rx, new_tx = [int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/rx_packets")), int(subprocess.getoutput(f"sudo cat /sys/class/net/{self.interface}/statistics/tx_packets"))]
            # print(f"New: {new_rx} | {new_tx}")
            self.f_pps = 0
            self.f_pps = (tx - new_tx) - (rx - new_rx)
