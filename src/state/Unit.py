from pygame.math import Vector2


class Unit:
    def __init__(self, position, speed, tile):
        """

        :type position: Vector2
        :type speed:    Vector2
        """
        self.position = position
        self.speed = speed
        self.tile = tile
        self.frame_index = 0.0
        self.max_frame_index = 5
