import os, platform

class OS_Info():
    _name: str
    _kernel: str
    _version: str
    _shell: str

class OS():
    info: OS_Info
    def __init__(self) -> None:
        self.info = OS_Info()
        self.info._name = platform.system()        
        self.info._version = platform.freedesktop_os_release().get("VERSION_ID", "N/A")
        self.info._kernel = platform.release()
        self.info._shell = os.environ.get("SHELL", "N/A")
