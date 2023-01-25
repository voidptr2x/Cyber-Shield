import requests

from ..tools.connection import *
from ..tools.os import *


class WebNotis:
    def __init__(self, ID, TOKEN, IFACE):
        """ https://discord.com/api/webhooks/1067821455179530301/RsvXv_-sfFjVR5mDjF2P2kYnDMBvaGEeUWtJhLG3eIgMT8bmENEew6E-QjIV8mRQw_yN """
        self.ID = ID
        self.TOKEN = TOKEN
        self.IFACE = IFACE
        self.url = f"https://discord.com/api/webhooks/1067821455179530301/RsvXv_-sfFjVR5mDjF2P2kYnDMBvaGEeUWtJhLG3eIgMT8bmENEew6E-QjIV8mRQw_yN"
        self.headers = {
            "Content-Type": "application/json"
        }
        
    
    def AttackNoti(self, ip, port, attackedport, pps, mbps, cpuload):
        self.Title = "Under attack"
        self.Description = f":shield: Filtering malicous IPS"
        self.Embed = {
            "username": "CyberShield Detection",
            "embeds": [{
                "fields": [
                    {
                    "name": "Server Information",
                    "value": f"`IP` - **[{ip}]**\n`Port` - **[{port}]**\n`Attacked Port` - **[{attackedport}]**",
                    "inline": False
                    }, 
                    {
                    "name": "Incoming PPS",
                    "value": f"[{pps}]",
                    "inline": False
                    }, 
                    {
                    "name": "Incoming MBPS",
                    "value": f"[{mbps}]",
                    "inline": False
                    },
                    {
                    "name": "CPU Load",
                    "value": f"[{cpuload}]",
                    "inline": False
                    }
                ],
            "title": self.Title,
            "description": self.Description,
            "color": "14177041"
            }]
        }
        requests.post(self.url, headers=self.headers, json=self.Embed)
    
    def ErrorNoti(self, py_err: str, discord: str):
        os = OS()
        self.Title = "Cyber Shield Application Error Report"
        self.Embed = {
            "username": "CyberShield Detection",
            "embeds": [{
                "fields": [{
                    "System IP:": f"System {system_ip(self.IFACE)}",
                    "OS": f"{os.info._name} | {os.info._version}",
                    "User's Discord": f"{discord}",
                    "Python Error": f"```{py_err}```",
                    "inline": False
                }],
            "title": self.Title,
            "color": "14177041"
            }]
        }
        g = requests.post(self.url, headers=self.headers, json=self.Embed).text
        print(g)
