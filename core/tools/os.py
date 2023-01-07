import os, sys, time, platform, subprocess

"""
This file needs functions to retrieve all these information that will be displayed on the console 

    "os_name_p": [5, 3],
        "os_kernel_p": [7, 3],
        "os_version_p": [6, 3],
        "shell_p": [8, 3]

OS Information from file /etc/os-release | Grabbing information from the file!

    PRETTY_NAME="Ubuntu 22.04.1 LTS"
    NAME="Ubuntu"
    VERSION_ID="22.04"
    VERSION="22.04.1 LTS (Jammy Jellyfish)"
    VERSION_CODENAME=jammy
    ID=ubuntu
    ID_LIKE=debian
    HOME_URL="https://www.ubuntu.com/"
    SUPPORT_URL="https://help.ubuntu.com/"
    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
    UBUNTU_CODENAME=jammy
"""
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
        self.retrieveKernel()
        self.retrieveShells()

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