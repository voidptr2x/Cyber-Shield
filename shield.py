import sys
from core.monitor import *
from core.utilities.extra import *

from discord_webhook import DiscordWebhook, DiscordEmbed
from core.tools.connection import *
from core.tools.os import *
from core.utilities.extra import *

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print(f"[ x ] Error, Invalid argument provided\r\nUsage: {sys.argv[0]} <interface>")
    exit()

max_pps = 0
c = 0
for arg in sys.argv:
    if arg == "-mp": max_pps = sys.argv[c+1]
    c += 1

try:
    commit = get_current_commit("update checker")
    commits = getAllCommits()

    if not commit: 
        print(f"[ + ] New update detected, Please update your app to verison {next(iter(commits))}")
        exit(0)

    print(f"Welcome To Cyber Shield v3.0 | {commit['version']}")
    for i in range(0, 5):
        print("Loading.....")
        time.sleep(1)
    CyberShield(sys.argv[1], max_pps)
except KeyboardInterrupt:
    print("\x1b[2J", end="")
    exit(0)
except Exception as err:
    tp, val, tb = sys.exc_info()
    os = OS()
    print("\x1b[2J")
    print(f"[ X ] Something went wrong.\r\n==================================================\r\n\x1b[31mPython Error\x1b[0m\r\nFilepath: {__file__}\nLine #: {sys.exc_info()[-1].tb_lineno}\nError: {err}\r\n==================================================\r\n")
    report_check = input("This problem can be solved and fix within a few minutes or hours if reported!\r\nDo you want to report this problem.? (Y/N):")
    update_info = get_current_commit("update checker")
    if report_check == "y" or report_check == "yes":
        discord_acc = input("What is your discord tag.? (Optional): ")
        if not discord_acc: discord_acc = "N/A"
        e = DiscordWebhook(url="https://discord.com/api/webhooks/1067821455179530301/RsvXv_-sfFjVR5mDjF2P2kYnDMBvaGEeUWtJhLG3eIgMT8bmENEew6E-QjIV8mRQw_yN")
        e.add_embed(DiscordEmbed(title='Cyber Shield Application Error Report:', description=f"System IP: {system_ip(sys.argv[1])}\nOS: {os.info._name}\nOS Version: {os.info._version}\nUser\'s Discord: {discord_acc}\nPython's Error:\nFilepath: ``{__file__}``\nLine #: ``{sys.exc_info()[-1].tb_lineno}``\nError:```{err}```", color='03b2f8'))
        e.execute()
    else: exit(0)