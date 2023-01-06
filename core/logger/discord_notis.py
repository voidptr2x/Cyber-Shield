# author: e991f665b7e62df5a54fdef19053a4e75117b89

# dependencies
import requests

class DiscordWebhook():
  def __init__(self, **kwargs):
    self.webhook = None # Default to None

    self.headers = {
      "User-Agent": "CyberShield (https://github.com/NefariousTheDev/Cyber-Shield, v3.0.0)",
      "Content-Type": "application/json"
    }

    if kwargs.get("url"):
      self.webhook = kwargs.get("url")

    if kwargs.get("id") and kwargs.get("token"):
      self.webhook = f"https://discord.com/api/v10/webhooks/{kwargs.get('id')}/{kwargs.get('token')}"

  def attack_notification(self, ip: str, port: str, attacked_port: str, pps: str, mbps: str, cpu: str):
    return self.send({
      "username": "CyberShield Detection",
      "embeds": [{
        "title": "Under attack",
        "description": ":shield: Filtering malicious IP addresses!",
        "color": 14177041,
        "fields": [{
          "name": "Server Information",
          "value": f"`IP` - **[{ip}]**\n`Port` - **[{port}]**\n`Attacked Port` - **[{attacked_port}]**"
        }, {
          "name": "Incoming PPS",
          "value": f"[{pps}]"
        }, {
          "name": "Incoming MBPS",
          "value": f"[{mbps}]"
        }, {
          "name": "CPU Load",
          "value": f"[{cpu}]"
        }]
      }]
    })

  def error_notification(self):
    return self.send({
      "username": "CyberShield Detection",
      "embeds": [{
        "title": "Error Detected",
        "color": 14177041,
        "fields": [{
          "name": ":warning: Error detected [filename]",
          "value": "On line [blablabla]"
        }]
      }]
    })

  def send(self, embed) -> bool:
    if not self.webhook:
      return False

    return requests.post(self.webhook, headers=self.headers, json=embed).status_code == 204