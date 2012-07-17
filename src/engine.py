import pygame
from display import Display
from events import EventManager
from task import TaskManager
from layer import LayerManager
from scene import SceneManager
from opengl import *

class Engine(object):
    def __init__(self, config):
        
        
        pygame.init()
        
        self.title = 'FoFiX' # Move to version.py
        
        self.config = config
        self.display = Display()
        
        self.task = TaskManager(self)
        self.events = EventManager()
        self.layer = LayerManager()
        self.scene = SceneManager()
        
        self.task.add(self.events)
        self.task.add(self.layer)
        self.task.add(self.scene)
        
        
        self.scene.create("GameScene")
        
        resolution = config['display', 'resolution']
        multisamples = config['display', 'multisamples']
        
        self.display.create_window(resolution, multisamples = multisamples)
        
        self.running = False
        
        self.run()
    
    def run(self):
        self.running = True
        
        while self.running:
        
            self.update()
            self.render()
            
            # Put the frame on screen
            pygame.display.flip()
    
    def update(self):
        self.task.run()
    
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.layer.render()
    
    def stop(self):
        self.running = False
        
        