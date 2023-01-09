import os, sys, time, subprocess

class Hardware_Info:
        cpu_cores: int
        cpu_name: str
        cpu_freq: str
        cpu_usage: str

        memory_type: str
        memory_capacity: str
        memory_used: str
        memory_free: str

        gpu_name: str
        gpu_cores: str
        gpu_freq: str
        gpu_usage: str

        hdd_name: str
        hdd_capacity: str
        hdd_used: str
        hdd_free: str
        hdd_usage: str

class Hardware():
        info: Hardware_Info
        def __init__(self) -> None:
                self.info = Hardware_Info()
                self.cpu_info = open("/proc/cpuinfo", "r")
                self.memory_info = open("/proc/meminfo", "r")

        def parseCPU(self) -> Hardware_Info:
                for line in self.cpu_info.split("\n"):
                        if line.startswith("cpu cores"):
                                self.info.cpu_cores = line.replace("cpu cores", "").replace(":", "").strip()

                        if line.startswith("model name"):
                                self.info.cpu_name = line.replace("model name", "").replace(":", "").strip()

                self.info.cpu_usage = subprocess.getoutput("top -bn1 | sed -n '/Cpu/p' | awk '{print $2}' | sed 's/..,//'")