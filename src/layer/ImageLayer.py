from .Layer import Layer


class ImageLayer(Layer):
    def __init__(self, cell_size, texture):
        super().__init__(cell_size, texture)

    def render(self, surface):
        surface.blit(self.texture, (0, 0))
