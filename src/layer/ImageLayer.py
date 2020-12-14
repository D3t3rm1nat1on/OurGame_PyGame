from .Layer import Layer


class ImageLayer(Layer):
    def __init__(self, texture, position):
        super().__init__(None, texture)
        self.position = position

    def render(self, surface):
        surface.blit(self.texture, self.position)
