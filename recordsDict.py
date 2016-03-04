# records_dict
#
# takes a directory name from analyze directory, yields a dictionary


import sys
import analyze
from analyze import *


def records_dict(solutionstextfile):
    genlist = []
    genlist.append(analyze.countlines.countlines(solutionstextfile))
    genlist.append(analyze.countforloops.countforloops(solutionstextfile))
    genlist.append(analyze.counthelpers.counthelpers(solutionstextfile))
    genlist.append(analyze.countifstatements.countifstatements(solutionstextfile))


        
    while True:
        solutionsdict = {}
        for gen in genlist:
            next = gen.next()
            solutionsdict[next[0]] = next[1]
        yield solutionsdict
        


# Example use

if __name__ == '__main__':
    a = records_dict("solutions/" + sys.argv[1] + "/solutions.txt")
    i = 0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"