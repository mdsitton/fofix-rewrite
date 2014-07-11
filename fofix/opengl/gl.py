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
from util import *

# Library Names
opengl32 = "opengl32"
glu32 = "glu32"

# Types
GLenum = c_uint
GLbitfield = c_uint
GLuint = c_uint
GLint = c_int
GLsizei = c_int
GLboolean = c_ubyte
GLbyte = c_char
GLshort = c_short
GLubyte = c_ubyte
GLushort = c_ushort
GLulong = c_ulong
GLfloat = c_float
GLclampf = c_float
GLdouble = c_double
GLclampd = c_double
GLvoid = None
GLchar = c_char

# Constants
GL_COLOR_BUFFER_BIT = 0x00004000
GL_DEPTH_BUFFER_BIT = 0x00000100


# Used when a function has no params instead of the (), it looks cleaner.
noParams = ()

# GLU
gluLookAtParams  = (c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double)
gluLookAt = CreateDllFunction( glu32, 'gluLookAt', None, gluLookAtParams )

gluPerspectiveParams = (c_double, c_double, c_double, c_double)
gluPerspective = CreateDllFunction( glu32, 'gluPerspective', None, gluPerspectiveParams )


# OLD OpenGL calls
glClearColorParams = (c_float, c_float, c_float, c_float)
glClearColor = CreateDllFunction( opengl32, 'glClearColor', None, glClearColorParams )

glClear = CreateDllFunction( opengl32, 'glClear', None, (GLbitfield,) )
