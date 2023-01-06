# author: e991f665b7e62df5a54fdef19053a4e75117b89

# dependencies
import os

class HardwareInformation():
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