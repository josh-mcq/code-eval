# solutionsfind.py
#
# A function that generates solutions files that match a given filename pattern


import os
import fnmatch

def solutions_find(filepat,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

# Example use

if __name__ == '__main__':
    solutions = solutions_find("*solutions.txt","solutions")
    for name in solutions:
        print name
