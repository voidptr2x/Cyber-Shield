# author: e991f665b7e62df5a54fdef19053a4e75117b89

# dependencies
import os

class HardwareInformation():
<<<<<<< Updated upstream
  cpu_info: list[str, str]
  cpu_usage: str

  mem_info: list[str, int]
  mem_name: str

  hdd_info: list[str, int]
  hdd_name: str

class Hardware():
  def __init__(self):
    self.info = HardwareInformation() # This is pointless

    self.info.cpu_info = self.get_cpu()
    self.info.cpu_usage = "0.00"

    self.info.mem_info = self.get_memory()
    self.info.mem_name = "N/A" # TODO: Make something to find this

    self.info.hdd_info = self.get_hdd()
    self.info.hdd_name = os.listdir("/sys/block")[0]

  # TODO: Move this to a utility file
  def get(self, data: str, string: str) -> str:
    return data.split(string)[1].split("\n")[0] or "N/A"

  def get_cpu(self) -> list[str, str]:
    with open("/proc/cpuinfo") as f:
      data = f.read()

      return {
        "cpu_name": self.get(data, "model name	: "),
        "cpu_count": self.get(data, "siblings	: "),
        "cpu_cores": self.get(data, "cpu cores	: "),
        "cpu_freq": self.get(data, "cpu MHz		: "),
      }

  def get_memory(self) -> list[str, int]:
    with open("/proc/meminfo") as f:
      data = f.read()

      # These values are in Kilobytes
      mem_total = int((self.get(data, "MemTotal:").split()[0]))
      mem_free = int((self.get(data, "MemFree:").split()[0]))

      return {
        "mem_total": mem_total / 1000,
        "mem_free": mem_free / 1000,
        "mem_used": (mem_total - mem_free) / 1000
      }

  def get_hdd(self) -> list[str, int]:
    stat = os.statvfs("/")

    total_size = stat.f_frsize * stat.f_blocks
    free_size = stat.f_frsize * stat.f_bfree

    return {
      "hdd_capacity": round(total_size / (1024 ** 3), 2),
      "hdd_free": round(free_size / (1024 ** 3), 2),
      "hdd_used": round((total_size - free_size) / (1024 ** 3), 2),
    }
=======
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
>>>>>>> Stashed changes
