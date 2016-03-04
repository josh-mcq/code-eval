# records_dict
#
# takes a directory name from pluggable directory, yields a dictionary


import sys
import pluggable
from analyze import *


def dict_creator(solutionstextfile):
    genlist = []
    genlist.append(pluggable.countlines.countlines(solutionstextfile))
    genlist.append(pluggable.countforloops.countforloops(solutionstextfile))
    genlist.append(pluggable.counthelpers.counthelpers(solutionstextfile))
    genlist.append(pluggable.countifstatements.countifstatements(solutionstextfile))


        
    while True:
        solutionsdict = {}
        for gen in genlist:
            next = gen.next()
            solutionsdict[next[0]] = next[1]
        yield solutionsdict  #one dictionary for each solution?
        


# Example use

if __name__ == '__main__':
    a = dict_creator("solutions/" + sys.argv[1] + "/solutions.txt")
    i = 0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"