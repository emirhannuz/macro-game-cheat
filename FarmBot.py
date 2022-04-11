import time
from MetinStoneManager import MetinStoneManager
from MouseEvent import MouseEvent
from WindowManager import WindowManager


class FarmBot:
    def __init__(self, windowManager: WindowManager, metinStoneManager: MetinStoneManager) -> None:
        self._windowManager = windowManager
        self._mouseEvent = MouseEvent(self._windowManager)
        self._metinStoneManager = metinStoneManager
        self._windowManager.set_foreground()

    def config(self) -> None:
        print("metinler arası beklenecek süre: ", str(
            self._metinStoneManager.get_wait_time()))

    def startMetinFarm(self) -> None:
        self.config()
        previous_metin = [-2, -2]
        while True:
            coordinate = self._metinStoneManager.search_metin_stone()
            if(self.checkIfCurrentPointEqualsToPreviousPoint(coordinate, previous_metin)):
                continue

            if coordinate[0] != -1:
                print({"x": coordinate[0], "y": coordinate[1]})
                self._mouseEvent.move(coordinate[0] + 40, coordinate[1] + 45)
                time.sleep(0.4)
                self._mouseEvent.click(x=coordinate[0] + 40, y=coordinate[1] + 45)
                previous_metin = coordinate
                time.sleep(self._metinStoneManager.get_wait_time())
            else:
                (x, y) = self._windowManager.center
                self._mouseEvent.move(x=x, y=y)
                self._mouseEvent.click(x=x, y=y)
                time.sleep(2)
            coordinate = []

    def checkIfCurrentPointEqualsToPreviousPoint(self, current: list[int], previous: list[int]) -> bool:
        if(previous[0] == current[0] and previous[1] == current[1]):
            print("koordinat önceki ile aynı başka aranıyor.")
            time.sleep(1)
            return True
        return False
