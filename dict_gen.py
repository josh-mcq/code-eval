import sys
import pluggable
#from pluggable.countlines
sys.path.insert(0, '/home/josh/code-eval/pluggable')
#maybe python this out so that it is more portable.
from pluggablefind import pluggable_find


def dict_creator(solutionstextfile):  #if this takes a single solutions file, how will all the solution files get run?
    pat = '(count.*?.py)+?'
    #for pluggable in pluggable_find(pat,"pluggable"):  #countlines, etc
    genlist = []
    genlist.append(pluggable.countlines.countlines(solutionstextfile))
    genlist.append(pluggable.countforloops.countforloops(solutionstextfile))
    genlist.append(pluggable.counthelpers.counthelpers(solutionstextfile))
    genlist.append(pluggable.countifstatements.countifstatements(solutionstextfile))


        
    while True:
        #for each generator in list, create a dict call each next()
        solutionsdict = {}
        for gen in genlist:
            next = gen.next()
            solutionsdict[next[0]] = next[1]
        yield solutionsdict  #one dictionary for each solution?
        



#def pluggablefind():  #generator function that yields function names like countforloops.py and other user generated ones.
    
# Example use

if __name__ == '__main__':
    import sys
    from pluggable import *
    sys.path.insert(0, '/home/josh/code-eval')
    from parsetext import parse_text
    a = dict_creator("solutions.txt")
    for line in a:
        print line
