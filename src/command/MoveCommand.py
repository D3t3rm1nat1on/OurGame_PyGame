from pygame.math import Vector2

from state import GameState, Unit, State

from .Command import Command


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
            self.unit.position.y = self.state.ground_level
            self.unit.speed = Vector2(self.unit.speed.x, 0)
        if self.unit.state == State.jumping_up and self.unit.speed.y >= 0:
            self.unit.state = State.jumping_down
        if self.unit.state == State.jumping_down and self.on_ground(self.state, self.unit):
            self.unit.state = State.running
