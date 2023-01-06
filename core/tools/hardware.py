import os, psutil, subprocess
        
class HardwareInformation():
    """
    Hardware
    """
    cpu_count: int
    cpu_name: str
    cpu_cores: str
    cpu_freq: str
    cpu_usage: str

    """
    Memory Information
    """
    memory_type: str
    memory_capacity: str
    memory_used: str
    memory_free: str

    """
    GPU Information
    """
    gpu_name: str
    gpu_cores: str
    gpu_freq: str
    gpu_usage: str

    """
    Hard drive Information
    """
    hdd_name: str
    hdd_capacity: str
    hdd_used: set
    hdd_free: str
    hdd_usage: str


"""
    Use Example:
    
    hdw = Hardware()
    hdw.info.OBJECTS_HERE
"""

# Get the Memory type from /proc/meminfo
with open('/proc/meminfo', 'r') as f:
    for line in f.readlines():
        if line.startswith('MemTotal'):
            memory_type = line.split(':')[1].strip()

 # Get the HDD name from /sys/block directory            
hdd_name = os.listdir('/sys/block')[0]

class Hardware():
    def __init__(self) -> None:
        self.info = HardwareInformation()
        self.__fetchCPU()
        self.__fetchMemory()
        self.__fetchHDD()

    def __fetchCPU(self) -> None:
        self.info.cpu_count = psutil.cpu_count()
        self.info.cpu_name = subprocess.getoutput("lscpu | sed -nr '/Model name/ s/.*:\s*(.*) @ .*/\\1/p'")
        
        for line in open("/proc/cpuinfo").read().split("\n"):
            if line.startswith("cpu cores"):
                self.info.cpu_cores = line.split(":")[1].strip()
                break
        
        self.info.cpu_usage = subprocess.getoutput("top -bn1 | sed -n '/Cpu/p' | awk '{print $2}' | sed 's/..,//'")

    def __fetchMemory(self) -> None:
        mem_info = psutil.virtual_memory()
        self.info.memory_type = memory_type
        self.info.memory_capacity = mem_info.total / (1024 ** 2)
        self.info.memory_used = mem_info.used / (1024 ** 2)
        self.info.memory_free = mem_info.free / (1024 ** 2)

    
    def __fetchHDD(self) -> None:
        disk_info = psutil.disk_usage('/')
        self.info.hdd_name = hdd_name
        self.info.hdd_capacity = disk_info.total / (1024 ** 3)
        self.info.hdd_usage = disk_info.used / (1024 ** 3)
        self.info.hdd_free = disk_info.free / (1024 ** 3)
