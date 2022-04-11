import win32con


class Click:
    def __init__(self, down, up, button) -> None:
        self.WM_DOWN = down
        self.WM_UP = up
        self.button = button

class LeftClick(Click):
    def __init__(self) -> None:
        Click.__init__(self, win32con.WM_LBUTTONDOWN, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON)


class RightClick(Click):
    def __init__(self) -> None:
        Click.__init__(self, win32con.WM_RBUTTONDOWN, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON)
