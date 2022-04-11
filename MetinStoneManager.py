from python_imagesearch.imagesearch import imagesearch
from MetinStone import MetinStone
from Player import Player
from tools import random_float


class MetinStoneManager:
    def __init__(self, metin_stone: MetinStone, player: Player) -> None:
        self._metin_stone = metin_stone
        self._player = player

    def search_metin_stone(self) -> list[int]:
        return imagesearch(self._metin_stone.image_path)

    def get_wait_time(self) -> float:
        return (((self._metin_stone.health / self._player.damage) * 100) / self._player.attack_speed) + random_float(0.4, 0.6)
