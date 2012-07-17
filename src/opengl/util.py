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

from ctypes import *
from ctypes.util import *
import platform

def get_library( name ):
    osName = platform.system()

    if osName == "Windows":
        lib = WinDLL(name)
    elif osName == "Darwin" or osName == "Linux":
        lib = CDLL(ctypes.util.find_library(name))
    return lib

class CreateDllFunction(object):
    def __init__(self, libName, name, returnType, params):
        osName = platform.system()
    
        if osName == "Windows":
            function = WINFUNCTYPE(returnType, *params)
        elif osName == "Darwin" or osName == "Linux":
            function = CFUNCTYPE(returnType, *params)
            
        address = getattr(get_library(libName), name)
        self.new_func = cast(address, function)
        
    def __call__(self, *args, **kwargs):
        return self.new_func(*args, **kwargs)
