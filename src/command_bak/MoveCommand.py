from pygame.math import Vector2

from .Command import Command
from src.state_bak import Unit
from src.state_bak import GameState


class MoveCommand(Command):

    unit: Unit
    state: GameState

    def __init__(self, state, unit):
        super().__init__()
        self.state = state
        self.unit = unit

    def run(self):
        self.unit.unique_movement()
        if self.unit.affected_by_gravity:
            self.unit.speed += self.state.gravity
        self.unit.position += self.unit.speed
        if self.on_ground(self.state, self.unit) and self.unit.speed.y >= 0 and self.unit.is_collision_able:
            self.unit.position.y = self.state.ground.y - self.unit.rect_collision.size[1]
            self.unit.speed = Vector2(self.unit.speed.x, 0)
        self.unit.rect_collision.topleft = self.unit.position
