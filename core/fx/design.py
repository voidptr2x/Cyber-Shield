import os

class ShieldFX():
    ui_path = "assets/ui.txt"
    ui_data: str
    def __init__(self) -> None:
        if not os.path.isfile(self.ui_path): return
        self.ui_data = open(self.ui_path, "r")
        
    def render_ui(self) -> str:
        return self.ui_data.read()
