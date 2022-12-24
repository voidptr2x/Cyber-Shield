import psutil

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

class Hardware():
    def show_hrwr_info():
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        cpu_percent = psutil.cpu_percent()

        print(f'CPU Count: {cpu_count}')
        print(f'CPU Frequency: {cpu_freq.current:.0f} MHz')
        print(f'CPU Utilization: {cpu_percent}%')

        mem_info = psutil.virtual_memory()
        mem_total = mem_info.total / (1024 ** 2)
        mem_used = mem_info.used / (1024 ** 2)
        mem_free = mem_info.free / (1024 ** 2)

        print(f'Total Memory: {mem_total:.0f} MB')
        print(f'Used Memory: {mem_used:.0f} MB')
        print(f'Free Memory: {mem_free:.0f} MB')

        disk_info = psutil.disk_usage('/')
        disk_total = disk_info.total / (1024 ** 3)
        disk_used = disk_info.used / (1024 ** 3)
        disk_free = disk_info.free / (1024 ** 3)

        print(f'Total Disk Space: {disk_total:.0f} GB')
        print(f'Used Disk Space: {disk_used:.0f} GB')
        print(f'Free Disk Space: {disk_free:.0f} GB')
    show_hrwr_info()