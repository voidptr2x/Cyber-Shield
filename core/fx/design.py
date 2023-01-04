import os, sys, time, subprocess

class ShieldFX():
    ui_path = "assets/ui.txt"
    ui_data: str
    def __init__(self) -> None:
        if os.path.isfile(self.ui_path) == False: return
        self.ui_data = open(self.ui_path, "r")
        
    def render_ui(self) -> str:
        return self.ui_data.read()
