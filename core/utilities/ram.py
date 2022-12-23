import sys, os, time, subprocess

class ram():
    ram=subprocess.getoutput(r" free -m | awk 'NR==2{printf  $3*100/$2 }'  | cut -c 1-5")
    print(f"{ram}%")