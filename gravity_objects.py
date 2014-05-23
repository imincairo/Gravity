# gravity_objects
import pygame


class Position():
    def __init__(self):
        self.coordinates = []

    def get_position(self):
        pass

    def get_previous(self):
        pass

    def get_next(self):
        pass


class GameObject(object):
    def __init__(self, event_manager, display_manager):
        self.event_manager = event_manager
        self.event_manager.subscribe(self)
        self.display_manager = display_manager
        self.position = Position()
        self.ticks = 0
        self.surface = None

    def get_rect(self):
        if self.surface:
            return self.surface.get_rect()
        else:
            return None

    def receive_event(self, event):
        pass

    def on_tick():
        pass

    def send_update(self):
        self.display_manager.receive_update((self.get_rect(),
                                             self.position.get_previous()))


class Character(GameObject):
    def __init__(self, event_manager):
        super(self.__class__, self).__init__(event_manager)
        self.x_coord = 0
        self.y_coord = 0

    def init(self):
        self.surface = pygame.Surface((25, 25)).convert()
        self.surface.fill((250, 250, 250))
        self.display_data['position'] = (self.x_coord, self.y_coord)
