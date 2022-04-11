import ctypes
from ctypes.wintypes import POINT
import time
import win32gui
import win32con
import win32api
from Click import Click, LeftClick

from WindowManager import WindowManager


class MouseEvent:
    def __init__(self, windowManager: WindowManager) -> None:
        self.__windowManager = windowManager

    def move(self, x: int = 0, y: int = 0) -> None:
        if x < 0 or y < 0:
            raise Exception("Koordinatlar sıfırdan büyük bir değer olmalı")
        win32api.SetCursorPos((x, y))

    @DeprecationWarning
    def left_click(self, x: int = None, y: int = None) -> None:
        if x and y:
            self.move(x, y)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
        time.sleep(0.2)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up

    @DeprecationWarning
    def right_click(self, x: int = None, y: int = None) -> None:
        if x and y:
            self.move(x, y)
        ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0)  # right down
        ctypes.windll.user32.mouse_event(16, 0, 0, 0, 0)  # right up


    def click(self, x: int = None, y: int = None, button: Click = LeftClick()) -> None:
        if not x and not y:
            current_position = self.get_cursor_position()
            x = current_position.x
            y = current_position.y

        self.__windowManager.set_foreground()
        lParam = self.get_long_param(x, y)
        win32gui.SendMessage(
            self.__windowManager.window, button.WM_DOWN, button.button, lParam)
        win32gui.SendMessage(
            self.__windowManager.window, button.WM_UP, None, lParam)
    
    def get_cursor_position(self) -> POINT:
        point = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
        return point
    
    def get_long_param(self,  x: int, y: int) -> int:
        return win32api.MAKELONG(x, y)
