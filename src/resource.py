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