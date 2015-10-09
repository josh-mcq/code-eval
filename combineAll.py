# combineAll


from pluggable import *
from itertools import izip
import sys
def combineWhoIsNext():
	lines = countlines.countlines("solutions/whoIsNext/solutions.txt")
	ifs = countifstatements.countifstatements("solutions/whoIsNext/solutions.txt")
	helpers = counthelpers.counthelpers("solutions/whoIsNext/solutions.txt")
	fors = countforloops.countforloops("solutions/whoIsNext/solutions.txt")
	seconds = countseconds.countseconds("solutions/whoIsNext/solutions.txt")
	#return [lines, ifs, helpers, fors, seconds]
	allthings = izip(lines,ifs,helpers,fors,seconds)
	return allthings

# Example use
# Must be called from code-eval/


if __name__ == '__main__':
    i=0
    #f = getattr(self, 'combineWhoIsNext')
    for thing in combineWhoIsNext():
        i+=1
        print thing
    print str(i) + "records printed"
