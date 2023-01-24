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
            print(line)
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


n = Nload()

print(n.get_nload_stats())