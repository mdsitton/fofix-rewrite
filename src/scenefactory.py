import glob

scenes = [n.replace(".py", "") for n in glob.glob("*scene.py")]

def create(engine, name, **args):
    m = __import__(name.lower())
    return getattr(m, name)(**args)
