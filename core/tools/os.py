# author: e991f665b7e62df5a54fdef19053a4e75117b89

# dependencies
import os
from os.path import exists

class OSInformation():
  os_release: dict[str, str]

  os_current_shell: str
  os_shells: list[str]

  os_kernel: str

class OS():
  def __init__(self):
    self.info = OSInformation() # This is pointless

    self.info.os_release = self.get_os_release()

    self.info.current_shell = self.get_current_shell()
    self.info.shells = self.get_shells()

    self.info.os_kernel = self.get_kernel()

  def get_os_release(self) -> dict[str, str]:
    variables = { }

    if not exists("/etc/os-release"):
      return variables

    with open("/etc/os-release") as f:
      data = f.read().split("\n")

      for line in data:
        if not "=" in line:
          continue

        x, y = line.split("=")

        variables[x.lower()] = y.strip("\"\"")

    return variables

  def get_current_shell(self) -> str:
    shell = os.environ.get("SHELL")

    if "/bin/" in shell: # Attempt to remove the path
      return shell.split("bin/")[1]

    return shell

  def get_shells(self) -> list[str]:
    shells = [ ]

    if not exists("/etc/shells"):
      return shells
    
    with open("/etc/shells") as f:
      data = f.read().split("\n")

      for line in data:
        if not line.startswith("/bin/"):
          continue

        shells.append(line[5:])

    return [ *set(shells) ]

  def get_kernel(self) -> str:
    with open("/proc/version") as f:
      return f.read().split(" ")[2:3][0]