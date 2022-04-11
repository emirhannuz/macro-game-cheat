import win32gui
import win32con


class KeyboardEvent:
    def __init__(self, window) -> None:
        self.__window = window

    def press(self, key) -> None:
        win32gui.SendMessage(self.__window, win32con.WM_CHAR, ord(key), 0)
