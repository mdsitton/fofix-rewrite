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

from fofix.display import Display
from fofix.events import EventManager
from fofix.task import TaskManager
from fofix.layer import LayerManager
from fofix.scene import SceneManager
#from fofix.opengl import *

import OpenGL.GL as gl

class Engine(object):
    ''' Necessary game structure, everything ties together here '''
    def __init__(self, config):
        
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

        width, height = resolution.split('x')
        width = int(width)
        height = int(height)

        multisamples = config['display', 'multisamples']
        
        self.display.create_window(width, height,  msaa = multisamples)
        
        self.running = False
        
        self.run()
    
    def run(self):
        self.running = True
        
        while self.running:
        
            self.update()
            self.render()
            
            # Put the frame on screen
            self.display.flip()
    
    def update(self):
        self.task.run()
    
    def render(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        self.layer.render()
    
    def stop(self):
        self.running = False
        
        