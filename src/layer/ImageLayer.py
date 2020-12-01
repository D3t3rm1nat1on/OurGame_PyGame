from .Layer import Layer


class ImageLayer(Layer):
    def __init__(self, texture):
        super().__init__(None, texture)

    def render(self, surface):
        surface.blit(self.texture, (0, 0))
