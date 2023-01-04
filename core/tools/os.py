import os, sys, time, platform, subprocess

class OSInformation():
    os_name: str
    os_version: str
    os_kernel: str

    os_shells: str
    os_current_shell: str

class OS():
    def __init__(self) -> None:
        self.info = OSInformation()

        self.retrieveOS()
        self.retrieveKernel()
        self.retrieveShells()

    def retrieveOS(self) -> None:
        self.info.os_name = open("/etc/os-release", "r").read().split("\n")[0].replace("PRETTY_NAME=\"", "").replace("NAME=\"", "").replace("\"", "")
        self.info.os_version = open("/etc/os-release", "r").read().split("\n")[2].replace("VERSION_ID=\"", "").replace("\"", "")

    def retrieveKernel(self) -> None:
        self.info.os_kernel = platform.release()

    def retrieveShells(self) -> None:
        self.info.os_shells = subprocess.getoutput("cat /etc/shells").split("\n")[1:]
        self.info.os_current_shell = subprocess.getoutput("echo $SHELL")
        