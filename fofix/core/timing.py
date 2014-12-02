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

import platform
import time
import sys

from fofix.core.pycompat import *

pyVer = sys.version_info

# Choose best time function for what we are running on
if pyVer.major == 3 and pyVer.minor >= 3:
    time_func = time.monotonic
elif platform.system() == 'Windows':
    time_func = time.clock
else:
    time_func = time.time

class Timer(object):
    ''' General purpose timing class. '''
    def __init__(self):
        self.currentTime = self.previousTime = self.time()

        self.tickDelta = 0

    def time(self):
        ''' Get current time in miliseconds '''
        return int(time_func() * 1000)

    def tick(self):
        ''' Get time delta since last call of tick '''
        self.previousTime = self.currentTime

        self.currentTime = self.time()

        self.tickDelta = self.currentTime - self.previousTime

        return self.tickDelta

class FpsCounter(Timer):
    ''' Helper class for Frames per Second calculation '''
    def __init__(self):

        super(FpsCounter, self).__init__()

        self.frames = 0
        self.fpsTime = 0
        self.fps = 0

    def tick(self):
        '''
        Calculate Time delta, and keep running total of frames since last
        fps calculation.
        Must be called once per rendered frame.
        '''
        super(FpsCounter, self).tick()

        self.fpsTime += self.tickDelta
        self.frames += 1

        return self.tickDelta

    def get_fps(self):
        ''' Calculate and return the estimated Frames Per Second '''
        if self.fpsTime == 0:
            self.fpsTime += 1

        self.fps = self.frames / (self.fpsTime / 1000.0)

        self.fpsTime = 0
        self.frames = 0

        return self.fps
