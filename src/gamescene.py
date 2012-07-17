from scene import Scene

class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
    
    def run(self):
        print "herp"
    
    def render(self):
        print "derp"
    
    def key_up(self, *args):
        print "hurrr"
        
    def key_down(self, *args):
        print "hurrr"