import os, sys, time, threading

from .utilities.pps import *
from .fx.design import *

class CyberShield():
    current_interface: str
    interfaces: list
    
    def __init__(self) -> None:
        #grab config information
        #display os, hardware, connection, motd and other information that doesn't update

        # LATER THING: start socket server here
        sfx = ShieldFX()
        print(sfx.render_ui())
        self.start_listener()

    def start_listener(self) -> None:
        # grab config information incase its needed for future features
        while True:
            pass