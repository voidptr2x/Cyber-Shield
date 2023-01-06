import requests


class WebNotis:
    def __init__(self, ID, TOKEN):
        self.ID = ID
        self.TOKEN = TOKEN
        self.url = f"https://discord.com/api/webhooks/{self.ID}/{self.TOKEN}"
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
    
    def ErrorNoti(self, ):
        self.Title = "Error Detected"
        self.Embed = {
            "username": "CyberShield Detection",
            "embeds": [{
                "fields": [{
                    "name": ":warning: Error detected [Filename]",
                    "value": "On line [blablabla]",
                    "inline": False
                }],
            "title": self.Title,
            "color": "14177041"
            }]
        }
        requests.post(self.url, headers=self.headers, json=self.Embed)

#p = WebNotis("WEBHOOK_ID",  "WEBHOOK_TOKEN")
#p.AttackNoti(ip="1.1.1.1", port="80", attackedport="1000", pps="100", mbps="1000", cpuload="3")
#p.ErrorNoti()