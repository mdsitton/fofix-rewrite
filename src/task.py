
class Task(object):
    def __init__(self):
        self._paused = False
        self.task = None
        self.engine = None
        
    def run(self):
        pass
    
    def started(self):
        pass
    
    def stopped(self):
        pass
    

class TaskManager(object):
    def __init__(self, engine):
        self.tasks = []
        self.engine = engine
        
    def add(self, func):
        if func not in self.tasks:
            func.task = self
            func.engine = self.engine
            self.tasks.append(func)
    
    def remove(self, func):
        if fun in self.tasks:
            self.tasks.remove(func)
    
    def pause(self, func):
        func._paused = True
    
    def resume(self, func):
        func._paused = False
    
    def run(self):
        for task in self.tasks:
            if not task._paused:
                task.run()
        