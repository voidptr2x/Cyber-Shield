import sys, os, time, psutil

class ram():
    ram=psutil.virtual_memory().percent
    print(f"{ram}")