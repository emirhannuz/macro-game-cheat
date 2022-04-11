class MetinStone:
    def __init__(self, image_path: str, name: str = None, health: int = None) -> None:
        self._image_path = image_path
        self._name = name
        self._health = health

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def image_path(self) -> str:
        return self._image_path
