import pygame

class Display(object):
    def __init__(self, title = "Game", icon = None):
        self.window       = None
        self.title        = title
        self.icon         = icon
        self.fullscreen   = False
        self.flags        = True
        self.multisamples = 0
    
    def create_window(self, resolution, fullscreen = False, 
                      flags = pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE, 
                      multisamples = 0):
    
        if fullscreen:
            flags |= pygame.FULLSCREEN
        
        self.flags = flags
        self.fullscreen   = fullscreen
        self.multisamples = multisamples
        resolution = resolution.split('x')
        self.resolution = (int(resolution[0]), int(resolution[1]))
        
        self.screen = pygame.display.set_mode(self.resolution, flags)
    
        pygame.display.set_caption(self.title)
        # pygame.mouse.set_visible(False)

    def flip(self):
        pygame.display.flip()

    def getVideoModes(self):
        return pygame.display.list_modes()