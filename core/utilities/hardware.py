import psutil
import platform
        
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
    memory_name: str
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
class Hardware():
    info: HardwareInformation
    def __init__(self) -> None:
        self.__fetchCPU()
        self.__fetchMemory()
        self.__fetchHDD()

    def __fetchCPU(self) -> None:
        self.info.cpu_count = psutil.cpu_count()
        self.info.cpu_name = "THIS IS NEEDED"
        self.info.cpu_freq = psutil.cpu_freq()
        self.info.cpu_usage = psutil.cpu_percent()

    def __fetchMemory(self) -> None:
        mem_info = psutil.virtual_memory()
        self.info.memory_name = "THIS IS NEEDED"
        self.info.memory_capacity = mem_info.total / (1024 ** 2)
        self.info.memory_used = mem_info.used / (1024 ** 2)
        self.info.memory_free = mem_info.free / (1024 ** 2)

    
    def __fetchHDD(self) -> None:
        disk_info = psutil.disk_usage('/')
        self.info.hdd_name = "THIS IS NEEDED"
        self.info.hdd_capacity = disk_info.total / (1024 ** 3)
        self.info.hdd_usage = disk_info.used / (1024 ** 3)
        self.info.hdd_free = disk_info.free / (1024 ** 3)
