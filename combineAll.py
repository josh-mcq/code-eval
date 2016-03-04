# combineAll
#
# Takes no parameters currently


from analyze import *
from itertools import izip
import sys

def combinergb():
	lines = countlines.countlines("solutions/rgb/solutions.txt")
	ifs = countifstatements.countifstatements("solutions/rgb/solutions.txt")
	helpers = counthelpers.counthelpers("solutions/rgb/solutions.txt")
	fors = countforloops.countforloops("solutions/rgb/solutions.txt")
	seconds = countseconds.countseconds("solutions/rgb/solutions.txt")
	allrecords = izip(lines,ifs,helpers,fors,seconds)
	return allrecords

# Example use
# Must be called from code-eval/


if __name__ == '__main__':
    i=0
    for record in combinergb():
        i+=1
        print record
    print str(i) + "records printed"
