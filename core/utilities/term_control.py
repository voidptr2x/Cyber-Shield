import os, time, sys

class TerminalControl:
    def placeText(position: list, label_c: list, label: str, value_c: list, value: str):
        print(f"\x1b[{position[0]};{position[1]}f\x1b[38;2;{label_c[0]};{label_c[1]};{label_c[2]}m", end="")
        print(f"{label}", end="")
        print(f"\x1b[38;2;{value_c[0]};{value_c[1]};{value_c[2]}m", end="")
        print(f"{value}", end="")
        # print("\x1b[37m", end="")

        
    def placeTextAlt(position: list, value: str):
        print(f"\x1b[{position[0]};{position[1]}f", end="")
        print(f"{value}", end="")
        print("\x1b[37m", end="")

    def move_cursor():
        print()