from .Unit import Unit


class Player(Unit):
    stamina: float
    max_speed_x: float

    def __init__(self, position, speed):
        super().__init__(position, speed)
        self.stamina = 100
        self.max_speed_x = 0.05

    def sprint(self):
        self.speed.x += 0.08
        self.stamina -= 0.5

    def unique_movement(self):
        # предел скорости
        if self.speed.x > self.max_speed_x:
            self.speed.x = self.max_speed_x
