import os, sys, time

class OSInformation():
    os_name: str
    os_version: str
    os_kernel: str

class OS():
    def __init__(self) -> None:
        self.info = OSInformation()
        self.os_name = os.name
        self.os_version = os.uname().release 
        self.os_kernel = os.uname() 
        pass