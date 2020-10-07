from pygame.math import Vector2


class GameState:
    def __init__(self):
        self.world_size = Vector2(1600, 900)
        self.ground = Vector2(0, 675)
        self.gravity = Vector2(0, 0.5)
        self.border_left = 0
        self.border_right = 300
