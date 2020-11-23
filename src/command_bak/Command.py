class Command:
    complete: bool

    def __init__(self):
        pass
    
    def run(self):
        raise NotImplementedError()

    def on_ground(self, state, unit):
        return unit.position.y + unit.rect_collision.size[1] >= state.ground.y
