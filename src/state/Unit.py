from pygame.math import Vector2


class Unit:
    def __init__(self, position, speed):
        """

        :type position: Vector2
        :type speed:    Vector2
        """
        self.position = position
        self.speed = speed
