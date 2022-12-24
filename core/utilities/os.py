import sys, os, platform

class os():
    def show_os_info():
        uname = platform.uname()
        print(f'System: {uname.system}')
        print(f'Node Name: {uname.node}')
        print(f'Release: {uname.release}')
        print(f'Version: {uname.version}')
        print(f'Machine: {uname.machine}')
        print(f'Processor: {uname.processor}')
    show_os_info()