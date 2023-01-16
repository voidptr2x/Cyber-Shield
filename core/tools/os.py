import os, sys, time, platform, subprocess

class OS_Info():
    _name: str
    _kernel: str
    _version: str
    _shell: str

class OS():
    info: OS_Info
    def __init__(self) -> None:
        self.info = OS_Info()
        self.os_release = open("/etc/os-release", "r")

        self.parseOS()
        self.retrieveShells()
        self.retrieveKernel()

    def parseOS(self) -> OS_Info:
        for line in self.os_release.read().split("\n"):
            if line.startswith("NAME=\""):
                self.info._name = line.replace("NAME=\"", "").replace("\"", "")

            if line.startswith("VERSION_ID=\""):
                self.info._version = line.replace("VERSION_ID=\"", "").replace("\"", "")
        self.os_release.close()
        return self.info

    def retrieveKernel(self) -> None:
        self.info._kernel = platform.release()

    def retrieveShells(self) -> None:
        self.info._shell = os.environ['SHELL']