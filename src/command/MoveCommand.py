from pygame.math import Vector2

from .Command import Command
import pygame

class MoveCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit

    def run(self):
        self.unit.speed += self.state.gravity
        self.unit.position += self.unit.speed
        if self.unit.position.y + self.unit.rect_collision.size[1] >= self.state.ground.y and self.unit.speed.y >= 0:
            self.unit.position.y = self.state.ground.y - self.unit.rect_collision.size[1]
            self.unit.speed = Vector2(self.unit.speed.x, 0)
        self.unit.rect_collision.x, self.unit.rect_collision.y = self.unit.position