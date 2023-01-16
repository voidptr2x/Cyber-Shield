import time

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
            rx, tx = [int(open(f"/sys/class/net/{self.interface}/statistics/rx_packets", "r").read()), int(open(f"/sys/class/net/{self.interface}/statistics/tx_packets", "r").read())]
            # print(f"Old: {rx} | {tx}")
            time.sleep(1)
            new_rx, new_tx = [int(open(f"/sys/class/net/{self.interface}/statistics/rx_packets", "r").read()), int(open(f"/sys/class/net/{self.interface}/statistics/tx_packets", "r").read())]
            # print(f"New: {new_rx} | {new_tx}")
            self.f_pps = 0
            self.f_pps = (tx - new_tx) - (rx - new_rx)
            print(self.f_pps, end="\r")
            
    """
    Run this to get all of the network statistics for all interfaces
    """
    def get_interface_statistics(self):
        """
        Returns a dictionary of the statistics for all network interfaces.

        The first key is the interface name, the second key is the statistics for that interface.

        The statistics are named as follows
        'bytesIn',  'packetsIn',  'errorsIn',  'dropsIn',  'fifoIn',  'frameIn',  'compressedIn',  'multicastIn',
        'bytesOut', 'packetsOut', 'errorsOut', 'dropsOut', 'fifoOut', 'frameOut', 'compressedOut', 'multicastOut'

        Example returned dictionary
        {
        'enp0s25': 
            {'bytesIn': '0', 'packetsIn': '0', 'errorsIn': '0', 'dropsIn': '0', 'fifoIn': '0', 'frameIn': '0',
            'compressedIn': '0', 'multicastIn': '0', 'bytesOut': '0', 'packetsOut': '0', 'errorsOut': '0',
            'dropsOut': '0', 'fifoOut': '0', 'frameOut': '0', 'compressedOut': '0', 'multicastOut': '0'},
        'wlp61s0':
            {'bytesIn': '1202280423', 'packetsIn': '1113475', 'errorsIn': '0', 'dropsIn': '0', 'fifoIn': '0',
            'frameIn': '0', 'compressedIn': '0', 'multicastIn': '0', 'bytesOut': '60239705', 'packetsOut':
            '308994', 'errorsOut': '0', 'dropsOut': '0', 'fifoOut': '0', 'frameOut': '0', 'compressedOut': '0',
            'multicastOut': '0'},
        'docker0':
            {'bytesIn': '0', 'packetsIn': '0', 'errorsIn': '0', 'dropsIn': '0', 'fifoIn': '0', 'frameIn': '0',
            'compressedIn': '0', 'multicastIn': '0', 'bytesOut': '0', 'packetsOut': '0', 'errorsOut': '0',
            'dropsOut': '0', 'fifoOut': '0', 'frameOut': '0', 'compressedOut': '0', 'multicastOut': '0'}
        }
        """

        # read network statistics of all interfaces
        with open("/proc/net/dev") as f:
            data = f.read()

        # remove training space, split on newline
        data = data.strip().split("\n")

        # headers for the data in the file
        headers = ['bytesIn',  'packetsIn',  'errorsIn',  'dropsIn',  'fifoIn',  'frameIn',  'compressedIn',  'multicastIn',
                   'bytesOut', 'packetsOut', 'errorsOut', 'dropsOut', 'fifoOut', 'frameOut', 'compressedOut', 'multicastOut']

        # dictionary to store {interface_name: {stat_name: stat_value, ...}, ...}
        ifaces_stats = {}

        # loop over all the lines, skip first 2 headers
        for line in data[3:]:
            line = line.split() # split the lines elements
            iface = line[0].strip(":") # extract interface name, w/o the included colon
            ifaces_stats[iface] = dict(zip(headers, line[1:])) # add the list of statistics to this interfaces entry in the dictionary

        return ifaces_stats
import os, sys, time, subprocess

class Netstat():
    data = ""
    connections = []
    def __init__(self) -> None:
        self.data = subprocess.getoutput("netstat -tn")
        self.remove_empty_element((self.data).split("\n"))
        """
            Splitting the response of the command
        """
        for line in (self.data).split("\n"):
            conn_info = self.remove_empty_element(line.split(" "))
            if "tcp" in conn_info[0]: (self.connections).append(self.remove_empty_element(line.split(" ")))

    def conns(self) -> list: return self.connections

    def remove_empty_element(self, arr: list) -> list:
        return list(filter(None, arr))
