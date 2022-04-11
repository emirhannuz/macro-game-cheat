import string
import win32gui
import win32api
import win32con
import re


class WindowManager:
    def __init__(self) -> None:
        self.__handle = None

    @property
    def window(self) -> tuple:
        return self.__handle

    @property
    def center(self) -> tuple:
        center = self.get_screen_size()
        return (center[0] // 2, center[1] // 2)

    def find_window(self, class_name, window_name: string = None) -> None:
        self.__handle = win32gui.FindWindow(class_name, window_name)
        print(self.__handle)

    def _window_enum_callback(self, hwnd, wildcard) -> None:
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self.__handle = hwnd

    def find_window_wildcard(self, wildcard) -> None:
        self.__handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self) -> None:
        win32gui.SetForegroundWindow(self.__handle)

    @DeprecationWarning
    def send_click_event(self, hwnd: int = None, x: int = None, y: int = None) -> None:
        lParam = win32api.MAKELONG(x, y)
        if hwnd == None:
            hwnd = self.__handle

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)

    def send_key_event(self, hwnd: int = None, key: str = "a") -> None:
        if hwnd == None:
            hwnd = self.__handle

        win32gui.SendMessage(hwnd, win32con.WM_CHAR, ord(key), 0)

    def list_inner_windows(self):
        print(self.get_inner_windows())

    def get_inner_windows(self) -> dict:
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
        hwnds = {}
        win32gui.EnumChildWindows(self.__handle, callback, hwnds)
        return hwnds

    def get_screen_size(self) -> tuple:
        self.set_foreground()
        result = win32gui.GetWindowRect(self.__handle)
        return (result[2], result[3])
