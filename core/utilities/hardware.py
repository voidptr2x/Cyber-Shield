import psutil

class hardware():
    def __setinfo(self) -> HardwareInformation:
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        mem_total = mem_info.total / (1024 ** 2)
        mem_used = mem_info.used / (1024 ** 2)
        mem_free = mem_info.free / (1024 ** 2)
        disk_info = psutil.disk_usage('/')
        disk_total = disk_info.total / (1024 ** 3)
        disk_used = disk_info.used / (1024 ** 3)
        disk_free = disk_info.free / (1024 ** 3)
        return f'CPU Count: {cpu_count}'
        return f'CPU Frequency: {cpu_freq.current:.0f} MHz'
        return f'CPU Utilization: {cpu_percent}%'
        return f'Total Memory: {mem_total:.0f} MB'
        return f'Used Memory: {mem_used:.0f} MB'
        return f'Free Memory: {mem_free:.0f} MB'
        return f'Total Disk Space: {disk_total:.0f} GB'
        return f'Used Disk Space: {disk_used:.0f} GB'
        return f'Free Disk Space: {disk_free:.0f} GB'
    show_hrwr_info()