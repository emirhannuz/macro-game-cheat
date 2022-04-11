from FarmBot import FarmBot
from MetinStone import MetinStone
from MetinStoneManager import MetinStoneManager
from Player import Player
from WindowManager import WindowManager


if __name__ == "__main__":
    windowManager = WindowManager()
    windowManager.find_window_wildcard(".*Aeldra*.")

    player = Player("Name", 10000, 191)
    metinStone = MetinStone("image_path",
                            "stone_name", 3500000)
    metinStoneManager = MetinStoneManager(metinStone, player)

    farmBot = FarmBot(windowManager, metinStoneManager)
    farmBot.startMetinFarm()
