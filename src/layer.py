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
        