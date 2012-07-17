import pygame
from task import Task

class Events(Task):
    def __init__(self):
        super(Events, self).__init__()
    
    def key_up(self, unicode, key, mod):
        pass
    
    def key_down(self, key, mod):
        pass
    
    def screen_active(self, gain, state):
        pass

        
class EventManager(Task):
    def __init__(self):
        super(EventManager, self).__init__()
        
        self.event = pygame.event
        
        self.listeners = []
    
    def add_listener(self, listener):
        self.engine.task.add(listener)
        if not listener in self.listeners:
            self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.engine.task.remove(listener)
            self.listeners.remove(listener)            
        
    def broadcast_event(self, function, *args):
        for listener in self.listeners:
            getattr(listener, function)(listener, *args)
    
    def run(self):
        
        eventName = None
        
        pygame.event.pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()
            elif event.type == pygame.ACTIVEEVENT:
                eventName = "screen_active"
            elif event.type == pygame.KEYDOWN:
                eventName = "key_down"
            elif event.type == pygame.KEYUP:
                eventName = "key_up"
            if eventName is not None:
                self.broadcast_event(eventName, event.dict)
            