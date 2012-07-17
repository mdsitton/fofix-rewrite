#####################################################################
# Frets on Fire X (FoFiX)                                           #
# Copyright (C) 2012 FoFiX Team                                     #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

import pygame

class Display(object):
    ''' Window creation '''
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