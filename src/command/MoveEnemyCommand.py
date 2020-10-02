import random

from pygame.math import Vector2

from .MoveCommand import MoveCommand


class MoveEnemyCommand(MoveCommand):
    def __init__(self, state, unit1, unit2):
        super().__init__(state, unit1)
        self.unit2 = unit2

    def run(self):
        super().run()
        # враг ушел за экран (успешный dodge)
        if self.unit.rect_collision.right <= -self.unit.size.x:
            rand = random.randint(self.state.world_size.x / 2, self.state.world_size.x)
            self.unit.position = Vector2(rand, 20)
            return 1
        # враг ударил игрока
        if self.unit.rect_collision.colliderect(self.unit2.rect_collision):
            rand = random.randint(self.state.world_size.x / 2, self.state.world_size.x)
            self.unit.position = Vector2(rand, 20)
        return 0
