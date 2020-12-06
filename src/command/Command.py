class Command:
    complete: bool

    def __init__(self):
        pass
    
    def run(self):
        raise NotImplementedError()

    def on_ground(self, state, unit):
        return unit.position.y >= state.ground_level
