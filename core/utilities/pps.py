import sys, os, time, subprocess

class PPS():
    old_rx: int
    old_tx: int

    new_rx: int
    new_tx: int

    pps: int
    def __init__(self, interface: str) -> None:
        self.interface = interface
        self.old_rx, self.old_tx = self.getPackets()
        time.sleep(1)
        self.new_rx, self.new_tx = self.getPackets()
        final_rx = self.old_rx - self.new_rx
        final_tx = self.old_tx - self.new_tx
        self.pps = int(final_tx - final_rx)

    """
    This functions returns rx and tx packets
    """
    def getPackets(self) -> list:
        return [int(subprocess.getoutput("sudo cat /sys/class/net/{0}/statistics/rx_packets".format(self.interface))), int(subprocess.getoutput("sudo cat /sys/class/net/{0}/statistics/tx_packets".format(self.interface)))]

    def retrievePPS(self) -> int: self.pps