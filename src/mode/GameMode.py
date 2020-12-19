class GameMode:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_load_level_requested(self):
        for observer in self.observers:
            observer.load_level_requested()

    def notify_show_game_requested(self) -> object:
        for observer in self.observers:
            observer.show_game_requested()

    def notify_show_menu_requested(self):
        for observer in self.observers:
            observer.show_menu_requested()

    def notify_show_pause_requested(self):
        for observer in self.observers:
            observer.show_pause_requested()

    def notify_show_perk_requested(self):
        for observer in self.observers:
            observer.show_perks_requested()

    def notify_quit_requested(self):
        for observer in self.observers:
            observer.quit_requested()

    def process_input(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def render(self, window):
        raise NotImplementedError()
