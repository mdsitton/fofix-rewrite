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

import ctypes as ct
import sdl2 as sdl

from fofix.task import Task
from fofix.keyconst import keymap, process_modkeys, process_key_char

class Events(Task):
    ''' Base event listener class '''
    def __init__(self):
        super(Events, self).__init__()
    
    def key_up(self, key, mod):
        pass
    
    def key_down(self, key, char, mod):
        pass
    
    def window_close(self):
        pass

    def window_resize(self, width, height):
        pass

        
class EventManager(Task):
    ''' Manages all events, and dispatches them to regestered listeners '''
    def __init__(self):
        super(EventManager, self).__init__()
        sdl.SDL_InitSubSystem(sdl.SDL_INIT_EVENTS)
        
        
        self.listeners = []
    
    def add_listener(self, listener):
        self.engine.task.add(listener)
        if not listener in self.listeners:
            self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.engine.task.remove(listener)
            self.listeners.remove(listener)            
        
    def broadcast_event(self, function, args):
        for listener in self.listeners:
            getattr(listener, function)(*args)
    
    def run(self):
        
        eventName = None

        event = sdl.SDL_Event()
        
        while sdl.SDL_PollEvent(ct.pointer(event)):

            if event.type == sdl.SDL_QUIT:
                self.engine.stop()

            elif event.type == sdl.SDL_KEYUP:
                eventName = 'key_up'

                data = (keymap[event.key.keysym.scancode],
                        process_modkeys(event.key.keysym.mod))

            elif event.type == sdl.SDL_KEYDOWN:
                eventName = 'key_down'
                data = (keymap[event.key.keysym.scancode],
                        process_key_char(event.key.keysym.sym),
                        process_modkeys(event.key.keysym.mod))

            elif event.type == sdl.SDL_WINDOWEVENT:
                winEvent = event.window.event

                if winEvent == sdl.SDL_WINDOWEVENT_CLOSE:
                    eventName = 'window_close'
                    data = tuple()
                elif winEvent == sdl.SDL_WINDOWEVENT_RESIZED:
                    eventName = 'window_resize'
                    data = (event.window.data1, event.window.data2)

            if eventName is not None:
                self.broadcast_event(eventName, data)
            