import os, sys, time, subprocess

class ShieldFX():
    ui_path = "assets/ui.txt"
    ui_data: str
    config_path = "assets/config.json"
    config_data: str
    rendered_ui: str
    def __init__(self) -> None:
        # check if file exists here to prevent errors
        self.config_path = open(self.config_path)
        self.ui_data = open(self.ui_path, "r")

        
    def parse(self) -> None:
        # create objects for JSON structures and fields for values
        pass
        
    def render_ui(self) -> str:
        # grab config information here
        return self.ui_data.read()
