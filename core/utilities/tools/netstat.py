import os, sys, time, subprocess

class Netstat():
    data = ""
    connections = []
    def __init__(self) -> None:
        self.data = subprocess.getoutput("netstat -tn")
        self.remove_empty_element((self.data).split("\n"))
        """
            Splitting the response of the command
        """
        for line in (self.data).split("\n"):
            conn_info = self.remove_empty_element(line.split(" "))
            if "tcp" in conn_info[0]: (self.connections).append(self.remove_empty_element(line.split(" ")))

    def conns(self) -> list: return self.connections

    def remove_empty_element(self, arr: list) -> list:
        return list(filter(None, arr))

n = Netstat()
print(n.connections[0][3])