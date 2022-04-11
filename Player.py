class Player:
    def __init__(self, name: str = None, damage: float = 100, attack_speed: int = 100) -> None:
        self._name = name
        self._damage = damage
        self._attack_speed = attack_speed

    @property
    def attack_speed(self) -> int:
        return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value) -> None:
        self._attack_speed = value

    @property
    def damage(self) -> int:
        return self._damage