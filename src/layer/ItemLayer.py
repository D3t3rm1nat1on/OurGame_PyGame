import math

from pygame.math import Vector2

from .UnitLayer import UnitLayer


class ItemLayer(UnitLayer):
    def __init__(self, cell_size, texture, game_state):
        super().__init__(cell_size, texture, game_state)

    def render(self, surface):
        for item in self.game_state.items:
            tile_x = math.floor(item.frame_index)
            animation = self.animations[item.state.value]
            tile_y = animation['row']
            if tile_x < animation['max_index']:
                item.frame_index += 0.25
            else:
                tile_x = 0
                item.frame_index = 0
            tile = Vector2(tile_x, tile_y)
            self.render_tile(surface, item.position, tile, item.size)
