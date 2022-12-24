import sys, os, time, platform, socket

class os():
    def show_os_info():
        os_name = platform.system()
        os_version = platform.release()
        processor = platform.processor()
        print(f"OS: {os_name} {os_version} ({processor})")
    show_os_info()