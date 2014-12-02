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

import math

from fofix.core.pycompat import *

from fofix.math import vector
from fofix.core import typeutils
import OpenGL.GL as gl

def zero_matrix(size):
    ''' Return zero filled matrix list of the requested size'''
    return [[0.0 for y in range(size)] for x in range(size)]

def identity(size):
    ''' Return an identity matrix list of the requested size '''
    return [[1.0 if x==y else 0.0 for y in range(size)] for x in range(size)]

def scale(size, value):
    if size == 4:
        value = value + [1.0,]
    return [[value[x] if x==y else 0.0 for y in range(size)] for x in range(size)]

def matrix_multiply(matrixA, matrixB):
    ''' Multiply matrixA with matrixB '''
    sizeA = len(matrixA)
    matOut = zero_matrix(sizeA)
    for i in range(sizeA):
        for j in range(sizeA):
            for k in range(sizeA):
                matOut[i][j] += matrixA[i][k] * matrixB[k][j]
    return matOut

def matrix_vector_multiply(matrix, vec):
    ''' Multiply matrix with vector '''
    matSize = len(matrix)
    vecSize = vec.size
    vecOut = vector.Vector(vecSize)
    for i in range(matSize):
        for j in range(matSize):
            vecOut.vector[i] += vec.vector[j] * matrix[j][i]
    return vecOut

def matrix_div(mat, scalar):
    ''' Divide a matrix by a scalar. '''
    size = len(mat)
    matOut = zero_matrix(size)
    for i in range(size):
        for j in range(size):
            matOut[i][j] = mat[j][i] / scalar
    return matOut

def transpose(mat):
    '''Transposes a NxN matrix.'''
    size = len(mat)
    out = zero_matrix(size)
    for i in range(size):
        for j in range(size):
            out[i][j]= mat[j][i]
    return out

###### Shear functions ####
def shearXY3(x, y):
    ''' Shear on XY. '''
    out = identity(3)
    out[0][3] = x
    out[1][3] = y
    return out

def shearYZ3(y, z):
    ''' Shear on YZ. '''
    out = identity(3)
    out[1][0] = y
    out[2][0] = z
    return out

def shearXZ3(x, z):
    ''' Shear on XZ. '''
    out = identity(3)
    out[0][1] = x
    out[2][1] = y
    return out

def shearXY4(x, y):
    ''' Shear on XY. '''
    out = identity(4)
    out[0][3] = x
    out[1][3] = y
    return out

def shearYZ4(y, z):
    ''' Shear on YZ. '''
    out = identity(4)
    out[1][0] = y
    out[2][0] = z
    return out

def shearXZ4(x, z):
    ''' Shear on XZ. '''
    out = identity(4)
    out[0][1] = x
    out[2][1] = y
    return out

###### Translate functions #####

def translate2(vector):
    ''' Translate by a vector.'''
    translate = identity(3)
    translate[2][0] = vector[0]
    translate[2][1] = vector[1]
    return translate

def translate3(vector):
    ''' Translate by a vector.'''
    translate = identity(3)
    translate[2][0] = vector[0]
    translate[2][1] = vector[1]
    translate[2][2] = vector[2]
    return translate

def translate4(vector):
    ''' Translate by a vector.'''
    translate = identity(4)
    translate[3][0] = vector[0]
    translate[3][1] = vector[1]
    translate[3][2] = vector[2]
    return translate


###### Rotate functions #####

def rotate2(point, theta):
    ''' Rotate around an axis.'''
    c = math.cos(math.radians(theta))
    s = math.sin(math.radians(theta))

    x1 = (point[0] - c) * (point[0]) - (-s * point[1])
    y1 = (point[1] - s) * (point[0]) - ( c * point[1])

    container = [[c, s, 0.0],
                 [-s, c, 0.0],
                 [x1, y1, 1.0]]

    return container

def rotate3(axis, theta):
    ''' Rotate around an axis.'''
    c = math.cos(math.radians(theta))
    s = math.sin(math.radians(theta))

    oneMinusCos = (1.0 - c)

    nAxis = vector.normalize(axis)

    x2 = nAxis[0] * nAxis[0]
    y2 = nAxis[1] * nAxis[1]
    z2 = nAxis[2] * nAxis[2]

    container = [[c + x2 * oneMinusCos, ((nAxis[1] * nAxis[0]) * oneMinusCos) + (nAxis[2] * s), ((nAxis[2] * nAxis[0]) * oneMinusCos) - (nAxis[1] * s)],
                [((nAxis[0] * nAxis[1]) * oneMinusCos) - (nAxis[2] * s), c + y2 * oneMinusCos, ((nAxis[2] * nAxis[1]) * oneMinusCos) + (nAxis[0] * s)],
                [((nAxis[0] * nAxis[2]) * oneMinusCos) + (nAxis[1] * s), ((nAxis[1] * nAxis[2]) * oneMinusCos) - (nAxis[0] * s), c + z2 * oneMinusCos]]
    return container

def rotate4(axis, theta):
    ''' Rotate around an axis.'''
    c = math.cos(math.radians(theta))
    s = math.sin(math.radians(theta))

    oneMinusCos = (1.0 - c)

    nAxis = vector.normalize(axis)

    x2 = nAxis[0] * nAxis[0]
    y2 = nAxis[1] * nAxis[1]
    z2 = nAxis[2] * nAxis[2]

    container = [[c + x2 * oneMinusCos, ((nAxis[1] * nAxis[0]) * oneMinusCos) + (nAxis[2] * s), ((nAxis[2] * nAxis[0]) * oneMinusCos) - (nAxis[1] * s), 0.0],
                 [((nAxis[0] * nAxis[1]) * oneMinusCos) - (nAxis[2] * s), c + y2 * oneMinusCos, ((nAxis[2] * nAxis[1]) * oneMinusCos) + (nAxis[0] * s), 0.0],
                 [((nAxis[0] * nAxis[2]) * oneMinusCos) + (nAxis[1] * s), ((nAxis[1] * nAxis[2]) * oneMinusCos) - (nAxis[0] * s), c + z2 * oneMinusCos, 0.0],
                 [0.0, 0.0, 0.0, 1.0]]
    return container

def rotate_origin2(theta):
    container = identity(3)
    container[0][0] = math.cos(theta)
    container[0][1] = math.sin(theta)
    container[1][0] = -math.sin(theta)
    container[1][1] = math.cos(theta)
    return container

###### Determinant functions ######

def det2(mat):
    ''' Determinant of a 2x2 matrix. '''
    return mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]

def det3(mat):
    ''' Determinant of a 3x3 matrix. '''
    return ( mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) -
            mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
            mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]) )

def det4(mat):
    ''' Determinant of a 4x4 matrix. '''

    sf00 = mat[2][2] * mat[3][3] - mat[3][2] * mat[2][3]
    sf01 = mat[2][1] * mat[3][3] - mat[3][1] * mat[2][3]
    sf02 = mat[2][1] * mat[3][2] - mat[3][1] * mat[2][2]
    sf03 = mat[2][0] * mat[3][3] - mat[3][0] * mat[2][3]
    sf04 = mat[2][0] * mat[3][2] - mat[3][0] * mat[2][2]
    sf05 = mat[2][0] * mat[3][1] - mat[3][0] * mat[2][1]
    sf06 = mat[1][2] * mat[3][3] - mat[3][2] * mat[1][3]
    sf07 = mat[1][1] * mat[3][3] - mat[3][1] * mat[1][3]
    sf08 = mat[1][1] * mat[3][2] - mat[3][1] * mat[1][2]
    sf09 = mat[1][0] * mat[3][3] - mat[3][0] * mat[1][3]
    sf10 = mat[1][0] * mat[3][2] - mat[3][0] * mat[1][2]
    sf11 = mat[1][1] * mat[3][3] - mat[3][1] * mat[1][3]
    sf12 = mat[1][0] * mat[3][1] - mat[3][0] * mat[1][1]
    sf13 = mat[1][2] * mat[2][3] - mat[2][2] * mat[1][3]
    sf14 = mat[1][1] * mat[2][3] - mat[2][1] * mat[1][3]
    sf15 = mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]
    sf16 = mat[1][0] * mat[2][3] - mat[2][0] * mat[1][3]
    sf17 = mat[1][0] * mat[2][2] - mat[2][0] * mat[1][2]
    sf18 = mat[1][0] * mat[2][1] - mat[2][0] * mat[1][1]

    inverse = zero_matatrix(4)
    inverse[0][0] = + (mat[1][1] * sf00 - mat[1][2] * sf01 + mat[1][3] * sf02)
    inverse[0][1] = - (mat[1][0] * sf00 - mat[1][2] * sf03 + mat[1][3] * sf04)
    inverse[0][2] = + (mat[1][0] * sf01 - mat[1][1] * sf03 + mat[1][3] * sf05)
    inverse[0][3] = - (mat[1][0] * sf02 - mat[1][1] * sf04 + mat[1][2] * sf05)

    inverse[1][0] = - (mat[0][1] * sf00 - mat[0][2] * sf01 + mat[0][3] * sf02)
    inverse[1][1] = + (mat[0][0] * sf00 - mat[0][2] * sf03 + mat[0][3] * sf04)
    inverse[1][2] = - (mat[0][0] * sf01 - mat[0][1] * sf03 + mat[0][3] * sf05)
    inverse[1][3] = + (mat[0][0] * sf02 - mat[0][1] * sf04 + mat[0][2] * sf05)

    inverse[2][0] = + (mat[0][1] * sf06 - mat[0][2] * sf07 + mat[0][3] * sf08)
    inverse[2][1] = - (mat[0][0] * sf06 - mat[0][2] * sf09 + mat[0][3] * sf10)
    inverse[2][2] = + (mat[0][0] * sf11 - mat[0][1] * sf09 + mat[0][3] * sf12)
    inverse[2][3] = - (mat[0][0] * sf08 - mat[0][1] * sf10 + mat[0][2] * sf12)

    inverse[3][0] = - (mat[0][1] * sf13 - mat[0][2] * sf14 + mat[0][3] * sf15)
    inverse[3][1] = + (mat[0][0] * sf13 - mat[0][2] * sf16 + mat[0][3] * sf17)
    inverse[3][2] = - (mat[0][0] * sf14 - mat[0][1] * sf16 + mat[0][3] * sf18)
    inverse[3][3] = + (mat[0][0] * sf15 - mat[0][1] * sf17 + mat[0][2] * sf18)

    return (  mat[0][0] * inverse[0][0]
            + mat[0][1] * inverse[0][1]
            + mat[0][2] * inverse[0][2]
            + mat[0][3] * inverse[0][3])

###### Inverse functions #####

def inverse2(mat):
    ''' Inverse of a 2x2 matrix '''
    det = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]

    inverse = zero_matrix(2)
    inverse[0][0] =   mat[1][1] / det
    inverse[0][1] = - mat[0][1] / det
    inverse[0][0] =   mat[1][0] / det
    inverse[0][1] = - mat[0][0] / det

    return inverse

def inverse3(mat):
    ''' Inverse of a 3x3 matrix.'''
    det = ( mat[0][0] * (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) -
            mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
            mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]) )

    invDet = 1 / det;

    temp = zero_matrix(3)

    temp[0][0] = (mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]) * invDet
    temp[0][1] = (mat[0][2] * mat[2][1] - mat[0][1] * mat[2][2]) * invDet
    temp[0][2] = (mat[0][1] * mat[1][2] - mat[0][2] * mat[1][1]) * invDet
    temp[1][0] = (mat[1][2] * mat[2][0] - mat[1][0] * mat[2][2]) * invDet
    temp[1][1] = (mat[0][0] * mat[2][2] - mat[0][2] * mat[2][0]) * invDet
    temp[1][2] = (mat[1][0] * mat[0][2] - mat[0][0] * mat[1][2]) * invDet
    temp[2][0] = (mat[1][0] * mat[2][1] - mat[2][0] * mat[1][1]) * invDet
    temp[2][1] = (mat[2][0] * mat[0][1] - mat[0][0] * mat[2][1]) * invDet
    temp[2][2] = (mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]) * invDet

    return temp

def inverse4(mat):
    ''' Inverse of a 4x4 matrix '''

    sf00 = mat[2][2] * mat[3][3] - mat[3][2] * mat[2][3]
    sf01 = mat[2][1] * mat[3][3] - mat[3][1] * mat[2][3]
    sf02 = mat[2][1] * mat[3][2] - mat[3][1] * mat[2][2]
    sf03 = mat[2][0] * mat[3][3] - mat[3][0] * mat[2][3]
    sf04 = mat[2][0] * mat[3][2] - mat[3][0] * mat[2][2]
    sf05 = mat[2][0] * mat[3][1] - mat[3][0] * mat[2][1]
    sf06 = mat[1][2] * mat[3][3] - mat[3][2] * mat[1][3]
    sf07 = mat[1][1] * mat[3][3] - mat[3][1] * mat[1][3]
    sf08 = mat[1][1] * mat[3][2] - mat[3][1] * mat[1][2]
    sf09 = mat[1][0] * mat[3][3] - mat[3][0] * mat[1][3]
    sf10 = mat[1][0] * mat[3][2] - mat[3][0] * mat[1][2]
    sf11 = mat[1][1] * mat[3][3] - mat[3][1] * mat[1][3]
    sf12 = mat[1][0] * mat[3][1] - mat[3][0] * mat[1][1]
    sf13 = mat[1][2] * mat[2][3] - mat[2][2] * mat[1][3]
    sf14 = mat[1][1] * mat[2][3] - mat[2][1] * mat[1][3]
    sf15 = mat[1][1] * mat[2][2] - mat[2][1] * mat[1][2]
    sf16 = mat[1][0] * mat[2][3] - mat[2][0] * mat[1][3]
    sf17 = mat[1][0] * mat[2][2] - mat[2][0] * mat[1][2]
    sf18 = mat[1][0] * mat[2][1] - mat[2][0] * mat[1][1]

    inverse = zero_matatrix(4)
    inverse[0][0] = + (mat[1][1] * sf00 - mat[1][2] * sf01 + mat[1][3] * sf02)
    inverse[0][1] = - (mat[1][0] * sf00 - mat[1][2] * sf03 + mat[1][3] * sf04)
    inverse[0][2] = + (mat[1][0] * sf01 - mat[1][1] * sf03 + mat[1][3] * sf05)
    inverse[0][3] = - (mat[1][0] * sf02 - mat[1][1] * sf04 + mat[1][2] * sf05)

    inverse[1][0] = - (mat[0][1] * sf00 - mat[0][2] * sf01 + mat[0][3] * sf02)
    inverse[1][1] = + (mat[0][0] * sf00 - mat[0][2] * sf03 + mat[0][3] * sf04)
    inverse[1][2] = - (mat[0][0] * sf01 - mat[0][1] * sf03 + mat[0][3] * sf05)
    inverse[1][3] = + (mat[0][0] * sf02 - mat[0][1] * sf04 + mat[0][2] * sf05)

    inverse[2][0] = + (mat[0][1] * sf06 - mat[0][2] * sf07 + mat[0][3] * sf08)
    inverse[2][1] = - (mat[0][0] * sf06 - mat[0][2] * sf09 + mat[0][3] * sf10)
    inverse[2][2] = + (mat[0][0] * sf11 - mat[0][1] * sf09 + mat[0][3] * sf12)
    inverse[2][3] = - (mat[0][0] * sf08 - mat[0][1] * sf10 + mat[0][2] * sf12)

    inverse[3][0] = - (mat[0][1] * sf13 - mat[0][2] * sf14 + mat[0][3] * sf15)
    inverse[3][1] = + (mat[0][0] * sf13 - mat[0][2] * sf16 + mat[0][3] * sf17)
    inverse[3][2] = - (mat[0][0] * sf14 - mat[0][1] * sf16 + mat[0][3] * sf18)
    inverse[3][3] = + (mat[0][0] * sf15 - mat[0][1] * sf17 + mat[0][2] * sf18)

    det = (  mat[0][0] * inverse[0][0]
           + mat[0][1] * inverse[0][1]
           + mat[0][2] * inverse[0][2]
           + mat[0][3] * inverse[0][3])

    inverse = matrix_div(inverse, det)

    return inverse

class Matrix(object):
    '''
    Matrix class wrapper.
    All operators are implemented in functions, and this class mainly
    acts as data validation/sorting based on input types.
    '''
    def __init__(self, size, data=None):
        self.size = size

        if data is None:
            self.matrix = identity(self.size)
        else:
            self.matrix = data

        self.c_matrix = typeutils.conv_list_2d(self.matrix, gl.GLfloat)


    def __mul__(self, other):
        if isinstance(other, vector.Vector):
            result = matrix_vector_multiply(self.matrix, other)
            return result

        elif isinstance(other, Matrix):
            if other.size != self.size:
                errText = 'size {}, expected {}'.format(other.size, self.size)
                raise ValueError(errText)
            else:
                result = matrix_multiply(self.matrix, other.matrix)
                return Matrix(self.size, data=result)
        else:
            return NotImplemented


    def __imul__(self, other):
        if isinstance(other, Matrix):
            if other.size != self.size:
                errText = 'size {}, expected {}'.format(other.size, self.size)
                raise ValueError(errText)
            else:
                self.matrix = matrix_multiply(self.matrix, other.matrix)
                self.c_matrix = typeutils.conv_list_2d(self.matrix, gl.GLfloat)
                return self
        else:
            return NotImplemented

    def i_scale(self, value):
        ''' Scale matrix instance in-place by Vector. '''
        if not isinstance(value, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(value)))
        if isinstance(value, vector.Vector):
            scaleMatlst = scale(self.size, value.vector)
            self *= Matrix(self.size, data=scaleMatlst)
            return self
        else:
            raise TypeError('Expected type: Vector')

    def scale(self, value):
        ''' Scale matrix instance by Vector, and return new matrix. '''
        if not isinstance(value, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(value)))
        if isinstance(value, vector.Vector):
            scaleMatlst = scale(self.size, value.vector)
            return self * Matrix(self.size, data=scaleMatlst)
        else:
            raise TypeError('Expected type: Vector')

    def det(self):
        ''' Calculate the determinant of a Matrix in-place. '''
        if self.size == 2:
            detT = det2(self.matrix)
        elif self.size == 3:
            detT = det3(self.matrix)
        elif self.size == 4:
            detT = det4(self.matrix)
        else:
            raise NotImplementedError('Matrix determinant of size {} is not implemented'.format(self.size))
        return detT

    def i_inverse(self):
        ''' Calculate the inverse of Matrix instance in-place. '''
        if self.size == 2:
            self.matrix = inverse2(self.matrix)
        elif self.size == 3:
            self.matrix = inverse3(self.matrix)
        elif self.size == 4:
            self.matrix = inverse4(self.matrix)
        else:
            raise NotImplementedError('Matrix inverse of size {} not implemented.'.format(self.size))

        self.c_matrix = typeutils.conv_list_2d(self.matrix, gl.GLfloat)
        return self

    def inverse(self):
        ''' Calculate the inverse of Matrix instance and return new Matrix. '''
        if self.size == 2:
            inv= inverse2(self.matrix)
        elif self.size == 3:
            inv = inverse3(self.matrix)
        elif self.size == 4:
            inv = inverse4(self.matrix)
        else:
            raise NotImplementedError('Matrix inverse of size {} not implemented.'.format(self.size))
        return Matrix(self.size, data=inv)

    def i_rotate(self, axis, theta):
        ''' Rotate Matrix instance in-place. '''
        if not isinstance(axis, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(axis)))

        if self.size == 2:
            rotMatList = rotate2(axis.vector, theta)
        elif self.size == 3:
            rotMatList = rotate3(axis.vector, theta)
        elif self.size == 4:
            rotMatList = rotate4(axis.vector, theta)
        else:
            raise NotImplementedError('Matrix rotate of size {} not implemented.'.format(self.size))
        self *= Matrix(self.size, data=rotMatList)
        return self

    def rotate(self, axis, theta):
        ''' Rotate Matrix instance and return new Matrix. '''
        if not isinstance(axis, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(axis)))

        if self.size == 2:
            rotMatList = rotate2(axis.vector, theta)
        elif self.size == 3:
            rotMatList = rotate3(axis.vector, theta)
        elif self.size == 4:
            rotMatList = rotate4(axis.vector, theta)
        else:
            raise NotImplementedError('Matrix rotate of size {} not implemented.'.format(self.size))
        return self * Matrix(self.size, data=rotMatList)

    def i_translate(self, vecA):
        ''' Translate Matrix instance in-place. '''
        if not isinstance(vecA, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(vecA)))

        if self.size == 2:
            transMatList = translate2(vecA.vector)
        elif self.size == 3:
            transMatList = translate3(vecA.vector)
        elif self.size == 4:
            transMatList = translate4(vecA.vector)
        else:
            raise NotImplementedError('Matrix translate of size {} not implemented.'.format(self.size))
        self *= Matrix(self.size, data=transMatList)
        return self

    def translate(self, vecA):
        ''' Translate Matrix instance and return new Matrix. '''
        if not isinstance(vecA, vector.Vector):
            raise TypeError('Expected Vector, got {}.'.format(type(vecA)))

        if self.size == 2:
            transMatList = translate2(vecA.vector)
        elif self.size == 3:
            transMatList = translate3(vecA.vector)
        elif self.size == 4:
            transMatList = translate4(vecA.vector)
        else:
            raise NotImplementedError('Matrix translate of size {} not implemented.'.format(self.size))
        return self * Matrix(self.size, data=transMatList)

    def i_transpose(self):
        ''' Transpose Matrix instance in-place. '''
        self.matrix = transpose(self.matrix)

        self.c_matrix = typeutils.conv_list_2d(self.matrix, gl.GLfloat)
        return self

    def transpose(self):
        ''' Transpose Matrix instance and return new Matrix. '''
        return Matrix(self.size, data=transpose(self.matrix) )

    def shear_xy(self, x, y):
        ''' Shear on XY and return new Matrix. '''
        if self.size == 3:
            transMatList = shearXY3(x, y)
        elif self.size == 4:
            transMatList = shearXY4(x, y)
        else:
            raise NotImplementedError('Matrix shearXY of size {} not implemented.'.format(self.size))
        return self * Matrix(self.size, data=transMatList)

    def i_shear_xy(self, x, y):
        ''' Shear on XY in-place. '''
        if self.size == 3:
            transMatList = shearXY3(x, y)
        elif self.size == 4:
            transMatList = shearXY4(x, y)
        else:
            raise NotImplementedError('Matrix shearXY of size {} not implemented.'.format(self.size))
        self *= Matrix(self.size, data=transMatList)
        return self

    def shear_yz(self, y, z):
        ''' Shear on YZ and return a new Matrix. '''
        if self.size == 3:
            transMatList = shearYZ3(y, z)
        elif self.size == 4:
            transMatList = shearYZ4(y, z)
        else:
            raise NotImplementedError('Matrix shearYZ of size {} not implemented.'.format(self.size))
        return self * Matrix(self.size, data=transMatList)

    def i_shear_yz(self, y, z):
        ''' Shear on YZ and return a new Matrix. '''
        if self.size == 3:
            transMatList = shearYZ3(y, z)
        elif self.size == 4:
            transMatList = shearYZ4(y, z)
        else:
            raise NotImplementedError('Matrix shearYZ of size {} not implemented.'.format(self.size))
        self *= Matrix(self.size, data=transMatList)
        return self

    def shear_xz(self, x, z):
        ''' Shear on XZ and return a new Matrix. '''
        if self.size == 3:
            transMatList = shearXZ3(x, z)
        elif self.size == 4:
            transMatList = shearXZ4(x, z)
        else:
            raise NotImplementedError('Matrix shearXZ of size {} not implemented.'.format(self.size))
        return self * Matrix(self.size, data=transMatList)

    def i_shear_xz(self, x, z):
        ''' Shear on XZ and return a new Matrix. '''
        if self.size == 3:
            transMatList = shearXZ3(x, z)
        elif self.size == 4:
            transMatList = shearXZ4(x, z)
        else:
            raise NotImplementedError('Matrix shearXZ of size {} not implemented.'.format(self.size))
        self *= Matrix(self.size, data=transMatList)
        return self

# Matrix-based functions the use the class instead of the functions directly

def ortho(left, right, bottom, top, zNear, zFar):
    ''' Orthographic Projection '''
    rtnMat = zero_matrix(4)
    rtnMat[0][0] = 2.0 / (right - left)
    rtnMat[1][1] = 2.0 / (top - bottom)
    rtnMat[2][2] = -2.0 / (zFar - zNear)
    rtnMat[3][0] = -(right + left) / (right - left)
    rtnMat[3][1] = -(top + bottom) / (top - bottom)
    rtnMat[3][2] = - (zFar + zNear) / (zFar - zNear)
    rtnMat[3][3] = 1
    return Matrix(4, data=rtnMat) 

def perspective(fov, aspect, znear, zfar):
    ''' Perspective projection matrix 4x4. FOVY'''
    rad = math.radians(fov)

    tanHalfFovy = math.tan(rad / 2.0)

    a = 1.0 / (aspect * tanHalfFovy)
    b = 1.0 / (tanHalfFovy)
    c = - (zfar + znear) / (zfar - znear)
    d = - (2.0 * zfar * znear) / (zfar - znear)
  
    out = [[  a, 0.0, 0.0, 0.0],
           [0.0,   b, 0.0, 0.0],
           [0.0, 0.0,   c,-1.0],
           [0.0, 0.0,   d, 0.0]]
    return Matrix(4, data=out)


def perspectiveX(fov, aspect, znear, zfar):
    ''' Perspective projection matrix 4x4. FOVX'''
    f = znear * math.tan((fov * PI / 360.0))

    xmax = f
    xmin = -f
    
    ymin = xmin / aspect
    ymax = xmax / aspect
    
    a = (2.0 * znear) / (xmax - xmin)
    b = (2.0 * znear) / (ymax - ymin)   
    c = -(zfar + znear) / (zfar - znear)
    d = -(2.0 * zfar * znear) / (zfar - znear)
    e = (xmax + xmin) / (xmax - xmin)
    f = (ymax + ymin) / (ymax - ymin)
    
    out = [[  a, 0.0, 0.0, 0.0],
           [0.0,   b, 0.0, 0.0],
           [  e,   f,   c,-1.0],
           [0.0, 0.0,   d, 0.0]]
    return Matrix(4, data=out)

def lookAt(eye, center, up):
    ''' Matrix 4x4 lookAt function.'''
    f = normalize(sub(center, eye))
    u = normalize(up)
    s = normalize(cross(f, u))
    u = cross(s, f)

    output = [[s[0], u[0], -f[0], 0.0],
              [s[1], u[1], -f[1], 0.0],
              [s[2], u[2], -f[2], 0.0],
              [-dot(s, eye), -dot(u, eye), dot(f, eye), 1.0]]
    return Matrix(4, data=output)

def project(obj, model, proj, viewport):
    ''' The most hacked together project code in the world. :| It works tho. '''
    projM = convert2Dto1D(proj)
    modelM = convert2Dto1D(model)

    T = m.Matrix(4)
    for r in range(4):
        for c in range(4):
            T[r][c] = 0.0
            for i in range(4):
                T[r][c] += projM[r + i * 4] * modelM[i + c *4]

    result = Vector(4)

    for r in range(4):
        result[r] = dot(T[r], obj)

    rhw = 1.0 / result[3]

    return [(1 + result[0] * rhw) * viewport[2] / 2.0 + viewport[0],
            (1 + result[1] * rhw) * viewport[3] / 2.0 + viewport[1],
            (result[2] * rhw) * (1 - 0) + 0, rhw]

def unproject(winx, winy, winz, modelview, projection, viewport):
    ''' Unproject a point from the screen and return the object coordinates. '''
    m = Matrix(4)
    IN = [0.0, 0.0, 0.0, 0.0]
    objCoord = [0.0, 0.0, 0.0]

    A = m.mulM(projection, modelview)
    m = m.inverse(A)

    IN[0] = (winx - viewport[0]) / viewport[2] * 2.0 - 1.0
    IN[1] = (winy - viewport[1]) / viewport[3] * 2.0 - 1.0
    IN[2] = 2.0 * winz - 1.0
    IN[3] = 1.0

    OUT = m.mulV(m, IN)
    if(OUT[3] == 0.0):
        return [0.0, 0.0, 0.0]

    OUT[3] = 1.0 / OUT[3]
    objCoord[0] = out[0] * out[3]
    objCoord[1] = out[1] * out[3]
    objCoord[2] = out[2] * out[3]
    return objCoord