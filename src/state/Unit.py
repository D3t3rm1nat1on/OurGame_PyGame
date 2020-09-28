from pygame.math import Vector2


class Unit:
    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), size=Vector2(40, 80)):
        self.position = position
        self.speed = speed
        self.size = size
