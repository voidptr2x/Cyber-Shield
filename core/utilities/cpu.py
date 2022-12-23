import sys, os, time, psutil

class cpu():
    def show_cpu_usage():
        cpu_usage = psutil.cpu_percent()
        print(f"CPU: {cpu_usage}%")
        time.sleep(0.5)
        os.system("clear")
    while True:
        show_cpu_usage()
        time.sleep(0.5)