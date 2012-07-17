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

import platform
import os

class Resource(object):
    def get_resource_path(self):
        '''
        Returns a path that holds the configuration files
        '''
        
        path = "."
        
        osName = platform.system()
        
        appname = 'FoFiX' #Version.PROGRAM_UNIXSTYLE_NAME - todo
        
        if osName == "Linux":
            path = os.path.expanduser("~/." + appname)
        elif osName == "Darwin" :
            path = os.path.expanduser("~/Library/Preferences/" + appname)
        elif osName == "Windows":
            path = os.path.join(os.environ["APPDATA"], appname)
            
        try:
            os.mkdir(path)
        except:
            pass
            
        return path