from task import Task

class Layer(Task):
    def shown(self):
        pass
        
    def hidden(self):
        pass
    
    def render(self):
        pass
    
class LayerManager(Task):
    def __init__(self):
        super(LayerManager, self).__init__()
        
        self.layers = []
        
    def add(self, func):
        if func not in self.layers:
            self.task.add(func)
            self.layers.append(func)
            func.shown()
    
    def remove(self, func):
        if func in self.layers:
            func.hidden()
            self.task.remove(func)
            self.layers.remove(func)
        
    def give_top(self):
        return self.layers[0]
    
    def remove_all(self):
        for layer in self.layers:
            self.remove(layer)
    
    def run(self):
        pass
    
    def render(self):
        for layer in self.layers:
            layer.render()
        