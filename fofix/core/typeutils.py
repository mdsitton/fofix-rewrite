#####################################################################
# Frets on Fire X (FoFiX)                                           #
# Copyright (C) 2014 FoFiX Team                                     #
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

from fofix.core.pycompat import *
import ctypes as ct

def cast_ptr(obj, ptrType):
    return ct.cast(obj, ct.POINTER(ptrType))

def to_c_str(text, hackRef=[], extList=False):
    ''' Convert python strings to null terminated c strings. '''
    # We only want to keep the cString data around for 1 call
    # This is a pretty terrible hack but oh well :(
    if not extList and len(hackRef) != 0:
        hackRef.remove(hackRef[0])
    cStr = ct.create_string_buffer(text.encode(encoding='UTF-8'))
    hackRef.append(cStr)
    return ct.cast(ct.pointer(cStr), ct.POINTER(ct.c_char))

def conv_list(listIn, cType):
    ''' Convert a python list into a ctypes array '''
    return (cType * len(listIn))(*listIn)

def conv_list_2d(listIn, cType):
    ''' Convert a python 2d list into a ctypes 2d array '''
    xlength = len(listIn)
    ylength = len(listIn[0])

    arrayOut = (cType * ylength * xlength)()

    for x in range(xlength):
        for y in range(ylength):
            arrayOut[x][y] = listIn[x][y]

    return arrayOut