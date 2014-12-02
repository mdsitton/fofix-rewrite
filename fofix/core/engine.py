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

from fofix.core import window
from fofix.core import context
from fofix.core.events import EventManager
from fofix.core.task import TaskManager
from fofix.core.layer import LayerManager
from fofix.core.scene import SceneManager
#from fofix.opengl import *

import OpenGL.GL as gl

class Engine(object):
    ''' Necessary game structure, everything ties together here '''
    def __init__(self, config):
        
        self.title = 'FoFiX' # Move to version.py
        
        self.config = config
        window.init_video()
        resolution = config['display', 'resolution']

        width, height = resolution.split('x')
        width = int(width)
        height = int(height)

        multisamples = config['display', 'multisamples']
        
        self.window = window.Window(width, height)

        # Forward Compatible Opengl 3.1 Core Profile Rendering Context
        # This was chosen as OpenGL 3.1 is the highest supported version on the
        # Sandy Bridge iGPU when on linux and windows.
        self.context = context.Context(3, 1, profile=context.PROFILE_CORE,
                                       flags=context.CONTEXT_FORWARD_COMPATIBLE,
                                       msaa=multisamples)

        self.window.make_current(self.context)


        self.task = TaskManager(self)
        self.events = EventManager()
        self.layer = LayerManager()
        self.scene = SceneManager()
        
        self.task.add(self.events)
        self.task.add(self.layer)
        self.task.add(self.scene)
        
        self.scene.create("GameScene")
        
        self.running = False
        
        self.run()
    
    def run(self):
        self.running = True
        
        while self.running:
        
            self.update()
            self.render()
            
            # Put the frame on screen
            self.window.flip()
    
    def update(self):
        self.task.run()
    
    def render(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        self.layer.render()
    
    def stop(self):
        self.running = False
        
        