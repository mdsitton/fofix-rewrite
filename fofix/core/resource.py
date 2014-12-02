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

''' Functions that deal with resources '''
import platform
import os
import sys

def get_path():

    # sys.path[0] in all cases i have observed is always ''
    # which when expanded out with os.path.realpath gets us the
    # current directory.
    # sys.path[1] 
    path0 = os.path.realpath('')
    path1 = os.path.realpath(sys.path[1])

    pathtest = os.sep.join(path0.split(os.sep)[:-1])

    if pathtest == path1:
        return path1
    else:
        return path0

def get_resource_path():
    '''
    Returns a path that holds the configuration files
    '''
    
    path = "."
    
    osName = platform.system()
    
    appname = 'FoFiX' # TODO - Version.PROGRAM_UNIXSTYLE_NAME
    
    if osName == "Linux":
        path = os.path.expanduser("~/.{}".format(appname))
    elif osName == "Darwin" :
        path = os.path.expanduser("~/Library/Preferences/{}".format(appname))
    elif osName == "Windows":
        path = os.path.expandvars('%APPDATA%\{}'.format(appname))
        
    try:
        os.mkdir(path)
    except:
        pass
        
    return path

