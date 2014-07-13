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

import ctypes

import sdl2 as sdl

# Fullscreen options
FS_OFF    = 1  # No fullscreen
FS_ON     = 2  # Regular fullscreen, sets monitor resolution
FS_HYBRID = 3  # Window will cover the monitor doesnt change resolution

def get_video_modes():
    modeCount = sdl.SDL_GetNumVideoDisplays()

    modes = []

    if modeCount < 1:
        print(sdl.SDL_GetError())
        sdl.SDL_ClearError()
    else:
        mode = sdl.SDL_DisplayMode()
        print (modeCount)
        for i in range(modeCount):
            err = sdl.SDL_GetDisplayMode(0, i, ct.pointer(mode))
            if err != 0:
                print(sdl.SDL_GetError())
                sdl.SDL_ClearError()
                continue
            modeData = {'x': mode.w, 'y': mode.h, 'hz': mode.refresh_rate}
            modes.append(modeData)

    return modes


def init_video():
    ''' Init SDL '''
    sdl.SDL_Init(0)
    sdl.SDL_InitSubSystem(sdl.SDL_INIT_VIDEO)

class Window(object):
    ''' Window creation '''
    def __init__(self, width, height, fullscreen = FS_OFF, 
                 title = 'Game', icon = None):

        self.title = title.encode('utf-8') # convert title to bytes
        self.icon = icon
        self.fullscreen = fullscreen
        self.width = width
        self.height = height

        self.flags = sdl.SDL_WINDOW_OPENGL | sdl.SDL_WINDOW_RESIZABLE
        

        if fullscreen == FS_OFF:
            self.posX = sdl.SDL_WINDOWPOS_CENTERED
            self.posY = sdl.SDL_WINDOWPOS_CENTERED

        elif fullscreen == FS_ON:
            self.posX = sdl.SDL_WINDOWPOS_UNDEFINED
            self.posY = sdl.SDL_WINDOWPOS_UNDEFINED
            self.flags |= sdl.SDL_WINDOW_FULLSCREEN

        else:
            self.posX = sdl.SDL_WINDOWPOS_UNDEFINED
            self.posY = sdl.SDL_WINDOWPOS_UNDEFINED
            self.flags |= sdl.SDL_WINDOW_FULLSCREEN_DESKTOP
        
        self.window = sdl.SDL_CreateWindow(self.title, self.posX, self.posY,
                        self.width, self.height, self.flags)

    def flip(self):
        sdl.SDL_GL_SwapWindow(self.window)

    def make_current(self, context):
        if context:
            window = self.window
            context.window = self
            context = context.context
        else:
            window = None
            context.window = None
            context = None

        sdl.SDL_GL_MakeCurrent(window, context)