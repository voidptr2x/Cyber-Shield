import time, requests, threading, subprocess, os, re

class nload_info():
    Curr: str
    Avg: str
    Min: str
    Max: str
    Ttl: str

    
class Nload():
    __data: str
    info: nload_info
    raw_text: str
    def __init__(self) -> None:
        self.info = nload_info()
        self.raw_text = ""

    def get_raw_text(self) -> str:
        return self.raw_text

    def runNload(self) -> None:
        while True:
            gg = self.get_nload_stats()
            self.info = self.__parseNload(gg)
            self.raw_text = f"Curr: {self.info.Curr}\nAvg: {self.info.Avg}\nMin: {self.info.Min}\nMax: {self.info.Max}\nTtl: {self.info.Ttl}"

    def __parseNload(self, data: str) -> nload_info:
        n = nload_info()
        for line in data.split("\n"):
            if "Curr:" in line: n.Curr = line.replace("Curr:", "").strip()
            else: n.Curr = "N/A"
            
            if "Avg:" in line: n.Avg = line.replace("Avg:", "").strip()
            else: n.Avg = "N/A"
            
            if "Min:" in line: n.Min = line.replace("Min:", "").strip()
            else: n.Min = "N/A"
            
            if "Max:" in line: n.Max = line.replace("Max:", "").strip()
            else: n.Max = "N/A"
            
            if "Ttl" in line: n.Ttl = line.replace("Ttl", "").strip()
            else: n.Ttl = "N/A"
        self.info = n
        return n
                
    def get_nload_stats(self) -> str:
        subprocess.getoutput("touch nload_results.txt; timeout 2 nload > nload_results.txt")
        info = ""
        new = open("nload_results.txt", "r").read()
        data = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]').sub('', new)

        for line in data.split("\n"):
            if "Incoming" in line:
                info = line.replace("==", "").replace("Incoming:", "Incoming:\n").replace("Avg:", "\nAvg:").replace("Min:", "\nMin: ").replace("Max:", "\nMax:").replace("Ttl:", "\nTtl")
            time.sleep(1)
        
        os.system("rm -rf nload_results.txt")
        return info

class Connection():
    upload: str
    download: str
    f_pps: int
    def __init__(self, iface: str) -> None:
        self.upload = ""
        self.download = ""
        self.interface = iface
        self.f_pps = 0

    def get_sys_ip(self) -> str:
        return requests.get("https://api.ipify.org").text

    def get_speed(self) -> list:
        threading.Thread(target=os.system, args=("speedtest > result.txt",)).start()
        for i in range(0, 30):

            time.sleep(1)
            results = open("result.txt", "r")
            speed = results.read()

            if "Upload: " in speed:
                for line in speed.split("\n"):
                    if line.startswith("Download:"): self.upload = line.replace("Download:", "").strip()
                    elif line.startswith("Upload:"): self.download = line.replace("Upload:", "").strip()
                results.close()
                return self.upload, self.download
        
        results.close()

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
            self.f_pps = (tx - new_tx) - (rx - new_rx)
            # print(self.f_pps, end="\r")
            
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
