import os, sys, time, subprocess

class OSInformation():
    os_name: str
    os_version: str
    os_kernel: str

class OS():
    def __init__(self) -> None:
        self.info = OSInformation()
        self.os_name = open("/etc/os-release", "r").read().split("\n")[0].replace("NAME=\"", "").replace("\"", "")
        self.os_version = open("/etc/os-release", "r").read().split("\n")[5].replace("VERSION_ID=\"", "").replace("\"", "")
        self.os_kernel = subprocess.getoutput("hostnamectl | grep Kernel").strip().replace("Kernel: ", "")