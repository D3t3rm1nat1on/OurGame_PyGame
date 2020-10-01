from pygame.math import Vector2

from .MoveCommand import MoveCommand


class MoveEnemyCommand(MoveCommand):
    def __init__(self, state, unit1, unit2):
        super().__init__(state, unit1)
        self.unit2 = unit2

    def run(self):
        super().run()
        if self.unit.position.x <= 40:
            self.unit.position = Vector2(self.state.world_size.x, 28)
        if not (self.unit2.position.x > self.unit.position.x + self.unit.size.x or
                self.unit2.position.x + self.unit2.size.x < self.unit.position.x or
                self.unit2.position.y > self.unit.position.y + self.unit.size.y or
                self.unit2.position.y + self.unit2.size.y < self.unit.position.y):
            self.unit.position = Vector2(self.state.world_size.x, 20)
