import psutil

class hardware():
    def __setinfo(self) -> HardwareInformation:
        
class HardwareInformation():
    """
    Hardware
    """
    cpu_count: int
    cpu: str
    cpu_cores: str
    cpu_freq: str
    cpu_usage: str

    """
    Memory Information
    """
    memory_capacity: str
    memory_used: str
    memory_free: str

    """
    Hard drive Information
    """
    hdd: str
    hdd_capacity: str
    hdd_used: set
    hdd_free: str