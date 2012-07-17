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
        