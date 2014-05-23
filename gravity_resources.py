# gravity_resources
import pygame
import gravity_objects as gos


MOVE_KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
SCREEN_SIZE = (800, 600)


class EventManager():
    def __init__(self):
        self.subscribers = []
        self.event_que = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def broadcast(self, event):
        for subscriber in self.subscribers:
            subscriber.receive_event(event)

    def que_event(self, event):
        self.event_que.append(event)

    def clear_que(self):
        self.event_que = []

    def get_events(self):
        if self.event_que:
            return self.event_que
        else:
            return None

    def manage(self):
        events = self.get_events()
        if events:
            self.clear_que()
            for event in events:
                self.broadcast(event)


class DisplayManager():
    def __init__(self):
        self.level = Level('Home')
        self.updates = []
        self.display = pygame.display.init()

    def receive_update(self, update):
        self.updates.append(update)

    def update(self):
        if self.updates:
            old_rects = []
            new_rects = []
            for update in self.updates:
                new_rects.append(update[0])
                if update[1]:
                    pass  # TODO get rect representing new rect at old position
            for rect in old_rects:
                pass  # TODO blit background over old sprites
            for rect in new_rect:
                pass  # TODO blit new sprites on background
            pygame.display.update(old_rects + new_rects)


    def update_all(self):
        pygame.display.flip()


class ClockController():
    def __init__(self, tick_interval=10):
        self.tick_interval = tick_interval

    def start(self):
        pass

    def stop(self):
        pass


class Level():
    def __init__(self, name, event_manager):
        self.name = name
        self.event_manager = event_manager
        self.game_objects = {}

    def load_level(self):
        if self.name == 'HOME':
            self.game_objects['background'] = gos.background(SCREEN_SIZE, 'grey')
            self.game_objects['ui'] = (gos.text_button('start', 'start')) # text, event action
            pass
        else:
            pass

    def build(self):
        for object_category in self.game_objects.keys():
            for game_object in self.game_objects[object_category]:
                game_object.send_update()
        pass


class KeyboardController():
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.event_manager.que_event(Event('quit'))
            if event.type == pygame.KEYDOWN and event.key in MOVE_KEYS:
                self.event_manager.que_event(Event('character_move',
                                                   event.key))
            if event.type == pygame.KEYUP and event.key in MOVE_KEYS:
                self.event_manager.que_event(Event('character_stop',
                                                   event.key))


class Event():
    def __init__(self, type, data=None):
        self.type = type
        self.data = data
