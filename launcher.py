#!/usr/bin/python
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

'''
Main game executable.
'''
# import argparse
import os

# Needed for pysdl2 to find the sdl dl's on windows
if os.name == 'nt':
    os.environ['PYSDL2_DLL_PATH'] = os.path.abspath(os.path.join('.', 'dll'))

from fofix.core.engine import Engine
from fofix.core.config import Config, define_all

def main():

    config = Config()
    
    define_all(config)
    
    # Load the main config file
    config.load('config.ini')
    
    # Start engine
    engine = Engine(config)
    
    # Write the config back to the ini file we loaded it from
    config.save()
    
if __name__ == '__main__':
    main()
    
    
