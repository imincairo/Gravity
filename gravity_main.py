# gravity_main
import pygame
import sys
from gravity_resources import (DisplayManager, EventManager,
                               KeyboardController, ClockController)


class App():
    def __init__(self):
        pygame.init()
        self.event_manager = EventManager()
        self.event_manager.subscribe(self)
        self.display_manager = None
        self.input_manager = KeyboardController(
            self.event_manager)
        self.clock_controller = ClockController()
        self.level = None

    def quit(self):
        pygame.quit()
        sys.exit()

    def receive_event(self, event):
        if event.type == 'quit':
            self.quit()

    def run(self):
        while True:
            self.input_manager.get_input()
            self.event_manager.manage()
            self.clock_controller.start()
