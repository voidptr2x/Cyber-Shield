import os, sys, time, subprocess



class ShieldFX():
    def __init__(self, file: str) -> None:
        self.file = file
        """
        Check if file exists to pervent errors
        """
        self.file_data = open(file)
        self.file_lines = self.file_data.split("\n")

    def parse(self) -> None:
        for line in self.file_lines:
            if not line.startswith(" ") or not line.startswith("//"): # Possiblitily of a new structue or comment line
            pass
            elif line.endswith("{")