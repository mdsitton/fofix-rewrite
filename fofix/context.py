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

import sdl2 as sdl

# Context Flags
CONTEXT_DEBUG = 0x1
CONTEXT_FORWARD_COMPATIBLE = 0x2
CONTEXT_ROBUST = 0x4
CONTEXT_RESET_ISOLATION = 0x8

# Context Profiles 
PROFILE_CORE = 1
PROFILE_COMPATIBILITY = 2
PROFILE_ES = 4

_fmap = {CONTEXT_DEBUG: sdl.SDL_GL_CONTEXT_DEBUG_FLAG,
         CONTEXT_FORWARD_COMPATIBLE: sdl.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG,
         CONTEXT_ROBUST: sdl.SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG,
         CONTEXT_RESET_ISOLATION: sdl.SDL_GL_CONTEXT_RESET_ISOLATION_FLAG}
        
_profileMap = {PROFILE_CORE: sdl.SDL_GL_CONTEXT_PROFILE_CORE,
               PROFILE_COMPATIBILITY: sdl.SDL_GL_CONTEXT_PROFILE_COMPATIBILITY,
               PROFILE_ES: sdl.SDL_GL_CONTEXT_PROFILE_ES}

def _convert_flags(value):
    ''' Helper function to convert context flags from ours, to SDL's '''
    flag = 0
    for item in _fmap:
        if value & item:
            flag |= _fmap[item]
    return flag


class Context(object):
    def __init__(self, major, minor, profile=None, flags=0, msaa=0,):

        self.major = major
        self.minor = minor
        self.profile = profile
        self.flags = flags
        self.msaa = msaa
        self.context = None
        self._window = None


        # Double buffering
        sdl.SDL_GL_SetAttribute(sdl.SDL_GL_DOUBLEBUFFER, 1)
        sdl.SDL_GL_SetAttribute(sdl.SDL_GL_CONTEXT_FLAGS, _convert_flags(flags))

        sdl.SDL_GL_SetAttribute(sdl.SDL_GL_CONTEXT_MAJOR_VERSION, major)
        sdl.SDL_GL_SetAttribute(sdl.SDL_GL_CONTEXT_MINOR_VERSION, minor)
        if profile is not None:
            sdl.SDL_GL_SetAttribute(sdl.SDL_GL_CONTEXT_PROFILE_MASK, 
                                    _profileMap[profile])

        if self.msaa > 0:
            sdl.SDL_GL_SetAttribute(sdl.SDL_GL_MULTISAMPLEBUFFERS, 1)
            sdl.SDL_GL_SetAttribute(sdl.SDL_GL_MULTISAMPLESAMPLES, self.msaa)

    @property
    def window(self):
        return self._window
    @window.setter
    def window(self, win):
        self._window = win

        if self.context == None:
            # Create context if not already created
            self.context = sdl.SDL_GL_CreateContext(self._window.window)