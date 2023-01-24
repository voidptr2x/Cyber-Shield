"""
Hardware Info Module

@title: Hardware.py
@description: Retrieving hardware information!
@since: 1/10/23

########################################################

To-do: Functions to grab GPU information!

########################################################

Application Output:

root@csmain:~/pytools# python3 hdw.py
Cyber Shield Hardware Module
CPU Name: Intel(R) Xeon(R) E-2288G CPU @ 3.70GHz
CPU Cores: 1
CPU Usage: 26.3
======================================
Memory Capacity: 4GB
Memory Free: 3GB
Memory Used: 1GB
======================================
HDD Capacity: 39GB
HDD Used: 5GB
HDD Free: 32GB
"""
import os, sys, time, subprocess, psutil

class Hardware_Info:
        cpu_cores: int
        cpu_name: str
        cpu_usage: str   

        memory_type: str ## Still needed (DDR3/4)
        memory_capacity: str
        memory_used: str
        memory_free: str

        """ ALL GPU INFO IS STILL NEEEDED """    
        gpu_name: str
        gpu_cores: str
        gpu_freq: str
        gpu_usage: str

        hdd_name: str ## Still needed
        hdd_capacity: str
        hdd_used: str
        hdd_free: str
        hdd_usage: str

class Hardware():
        info: Hardware_Info
        def __init__(self) -> None:
                self.info = Hardware_Info()
                self.cpu_info, self.mem_info, self.hdd_info = self._retrieveInfo()

        def updateInfo(self) -> None:
                self._retrieveInfo()
                self.parseHardware()
                self.parseMEM()
                self.retrieveHDD()

        def _retrieveInfo(self) -> None:
                cpu_info, mem_info, hdd_info = [open("/proc/cpuinfo", "r"), open("/proc/meminfo", "r"), psutil.disk_usage("/")]
                cpu, mem = [cpu_info.read(), mem_info.read()]

                cpu_info.close()
                mem_info.close()

                return [cpu, mem, hdd_info]

        def parseHardware(self):
                for line in self.cpu_info.split("\n"):
                        if line.startswith("cpu cores"): self.info.cpu_cores = line.replace("cpu cores", "").replace(":", "").strip()

                        if line.startswith("model name"): self.info.cpu_name = line.replace("model name", "").replace(":", "").strip().split("@")[0]

                self.info.cpu_usage = subprocess.getoutput("top -bn1 | sed -n '/Cpu/p' | awk '{print $2}' | sed 's/..,//'")

        def parseMEM(self):
                for line in self.mem_info.split("\n"):
                        if line.startswith("MemTotal:"): self.info.memory_capacity = round(int(line.replace("MemTotal:", "").replace("kB", "").strip()) / 1000000)

                        if line.startswith("MemFree:"): self.info.memory_free = round(int(line.replace("MemFree:" ,"").replace("kB", "").strip()) / 1000000)

                self.info.memory_used = self.info.memory_capacity - self.info.memory_free

        def retrieveHDD(self):
                self.info.hdd_capacity = round(self.hdd_info.total / (2**30))
                self.info.hdd_used = round(self.hdd_info.used / (2**30))
                self.info.hdd_free = round(self.hdd_info.free / (2**30))

                return self.info
