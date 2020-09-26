from pygame.math import Vector2


class Unit:
    def __init__(self, position = Vector2(10, 20), speed = Vector2(2, 0), size = Vector2(30, 60)):
        self.position = position
        self.speed = speed
        self.size = size