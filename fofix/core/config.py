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

from configparser import ConfigParser
import os

from fofix.core import resource

class Config(object):
    ''' Configuration file manager
        read, save, edit, and store game configuration data '''
    def __init__(self):
        self.config       = ConfigParser(interpolation=None)
        
        self.configfile = None
        
        self.configTypes = {}
    
    def load(self, fileName):
        if fileName:
            if not os.path.isfile(fileName):
                path = resource.get_resource_path()
                fileName = os.path.join(path, fileName)

        self.config.read(fileName)
        self.configfile = fileName
    
    def save(self):
        file = open(self.configfile, "w")
        self.config.write(file)
        file.close()
        
    def add_section(self, section):
        self.config.add_section(section)
        self.configTypes[section] = {}

    def __setitem__(self, key, value):        
        if not self.config.has_section(key[0]):
            self.add_section(key[0])
        self.config[key[0]][key[1]] = value
        self.configTypes[key[0]][key[1]] = key[2]
        
        
    def __getitem__(self, key):
        value = self.config[key[0]][key[1]]
        type = self.configTypes[key[0]][key[1]]
        
        # The following checks what type value should be, 
        # converts, and returns it
        
        if type == bool:
            return self.config[key[0]].getboolean(key[1])
        else:
            return type(value)

def define_all(config):
    ''' All configuration values '''
    
    config['display', 'resolution', str] = '800x600'
    config['display', 'multisamples', int] = '4'
    config['display', 'fullscreen', bool] = 'false'