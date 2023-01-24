import time
class TerminalControl:
    def placeText(position: list, label_c: list, label: str, value_c: list, value: str) -> None:
        print(f"\x1b[{position[0]};{position[1]}f\x1b[38;2;{label_c[0]};{label_c[1]};{label_c[2]}m{label}\x1b[38;2;{value_c[0]};{value_c[1]};{value_c[2]}m{value}\x1b[0m", end="")

    def listText(position: list, value: str) -> None:
        c = position[0]
        for t in value.split("\n"):
            TerminalControl.place_text([c, position[1]], t)
            c+=1

    def listText_c(position: list, color: list, value: str) -> None:
        c = position[0]
        for t in value.split("\n"):
            TerminalControl.place_c_text([c, position[1]], color, t)
            c+=1
        
    def placeTextAlt(position: list, value: str):
        print(f"\x1b[{position[0]};{position[1]}f", end="")
        print(f"{value}", end="")
        print("\x1b[37m", end="")

    def move_cursor(position: list):
        print(f"\x1b[{position[0]};{position[1]}f", end="")

    def place_text(position: list, value: str):
        print(f"\x1b[{position[0]};{position[1]}f", end="")
        print(f"{value}", end="")

    def place_c_text(position: list, c: list, value: str):
        print(f"\x1b[{position[0]};{position[1]}f", end="")
        print(f"\x1b[38;2;{c[0]};{c[1]};{c[2]}m{value}\x1b[0m", end="")

    def ansiColor(c: list) -> str:
        return f"\x1b[38;2;{c[0]};{c[1]};{c[2]}m"