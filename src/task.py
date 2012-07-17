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
    
    def is_paused(self):
        return self._paused
    
    def set_pause(self, value):
        self._paused = value

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
        func.set_pause(True)
    
    def resume(self, func):
        func.set_pause(False)
    
    def run(self):
        for task in self.tasks:
            if not task.is_paused:
                task.run()
        