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

import importlib
from fofix.core.resource import get_path

# dictionary of scenes
# TODO - implement a system that auto detects scenes
# basically enforce a specific naming scheme on scenes
# so that we can get the scene name and determine that its 
# actually a scene from the file name.
# something like scene_SceneName.py or SceneName_scene.py could work.
sceneInfo = {
   "GameScene": "fofix.scenes.gamescene"
}

def create(name, **args):
    scene_name = importlib.import_module(sceneInfo[name])
    return getattr(scene_name, name)(**args)