from pygame import Vector2
from pygame import Surface
from pygame import Rect
import pygame.image


class Layer:
    def __init__(self, cell_size, texture):
        """

        :type cell_size: Vector2
        :type texture:   str
        """
        self.cell_size = cell_size
        self.texture = pygame.image.load(texture)

    def render_tile(self, surface, position, tile, tile_size=Vector2(1, 1)):
        """
        Draw tile from texture on surface

        :type tile_size:Vector2
        :type surface:  Surface
        :type position: Vector2
        :type tile:     Vector2
        """
        sprite_point = position.elementwise() * self.cell_size
        texture_point = tile.elementwise() * self.cell_size
        texture_rect = Rect(int(texture_point.x * tile_size.x), int(texture_point.y), self.cell_size.x * tile_size.x,
                            self.cell_size.y * tile_size.y)
        surface.blit(self.texture, sprite_point, texture_rect)

    def render(self, surface):
        """

        :type surface: Surface
        """
        raise NotImplementedError
