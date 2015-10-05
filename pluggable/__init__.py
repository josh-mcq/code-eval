from os.path import dirname, basename, isfile
import os
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]

#for module import path
#IMPORT_PATH = "/home/josh/code-eval"
IMPORT_PATH = ('/').join(os.getcwd().split('/')[:-1])

