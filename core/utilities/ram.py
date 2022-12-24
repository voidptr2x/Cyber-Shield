import sys, os, time, psutil

class ram():
    def show_ram_usage():
        ram_usage = psutil.virtual_memory().percent
        print(f"RAM: {ram_usage}%")
        time.sleep(0.5)
        os.system("clear")
    while True:
        show_ram_usage()
        time.sleep(0.5)