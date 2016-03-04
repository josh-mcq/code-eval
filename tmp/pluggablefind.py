# pluggablefind.py
#
# A function that generates solutions files that match a given filename pattern


import os
import fnmatch
import re

def pluggable_find(filepat,top):
    files =  os.walk(top).next()[2]
    for f in files:
    	yield f
        

# Example use

if __name__ == '__main__':
	pat = '(count.*?.py)+?'
	pluggables = pluggable_find(pat,"pluggable")
	for name in pluggables:
		print name
