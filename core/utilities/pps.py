import sys, os, time, subprocess

class PPS():
    old_rx: int
    old_tx: int

    new_rx: int
    new_tx: int

    pps: int
    def __init__(self, interface: str) -> None:
        self.interface = interface


class OldPPS:
    old_rx = 0
    old_tx = 0
    new_rx = 0
    new_tx = 0
    pps = 0

    def set_old(rx, tx):
        PPS.old_rx = rx
        PPS.old_tx = tx

    def set_new(rx, tx):
        PPS.new_rx = rx
        PPS.new_tx = tx

    def GetPPS():
        final_rx = PPS.old_rx - PPS.new_rx
        final_tx = PPS.old_tx - PPS.new_tx
        PPS.pps = final_tx - final_rx
        return PPS.pps

    def GetInterface():
        return subprocess.getoutput("ifconfig").split(":")[0]

    def RxPackets():
        return subprocess.getoutput("sudo cat /sys/class/net/{0}/statistics/rx_packets".format(PPS.GetInterface()))

    def TxPackets():
        return subprocess.getoutput("sudo cat /sys/class/net/{0}/statistics/tx_packets".format(PPS.GetInterface()))

    def run():
        while(1):
            PPS.set_old(int(PPS.RxPackets()), int(PPS.TxPackets()))
            time.sleep(1)
            PPS.set_new(int(PPS.RxPackets()), int(PPS.TxPackets()))
            final_pps = PPS.GetPPS()