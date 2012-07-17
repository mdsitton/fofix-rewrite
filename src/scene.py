from layer import Layer
from task import Task
from events import Events
import scenefactory

class Scene(Layer, Events):
    def __init__(self):
        super(Scene, self).__init__()
        
    def shown(self):
        self.engine.events.add_listener(self)
        
    def hidden(self):
        self.engine.events.remove_listener(self)
    
    def run(self):
        pass
    
    def render(self):
        pass

class SceneManager(Task):
    def __init__(self):
        super(SceneManager, self).__init__()
        
        self.currentScene = None
        self.sceneName = None
        
        self.layer = None
    
    def create(self, name, **args):
        self.layer = self.engine.layer
        if self.currentScene:
            self.remove()
        self.currentScene = scenefactory.create(self.engine, name, **args)
        self.layer.add(self.currentScene)
        self.layer.add(self.currentScene)
        
    def remove(self):
        self.layer.remove(self)
        self.current
        