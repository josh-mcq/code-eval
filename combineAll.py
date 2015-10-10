# combineAll


from pluggable import *
from itertools import izip
import sys
def combinerecoverSecret():
	lines = countlines.countlines("solutions/recoverSecret/solutions.txt")
	ifs = countifstatements.countifstatements("solutions/recoverSecret/solutions.txt")
	helpers = counthelpers.counthelpers("solutions/recoverSecret/solutions.txt")
	fors = countforloops.countforloops("solutions/recoverSecret/solutions.txt")
	seconds = countseconds.countseconds("solutions/recoverSecret/solutions.txt")
	allrecords = izip(lines,ifs,helpers,fors,seconds)
	return allrecords

# Example use
# Must be called from code-eval/


if __name__ == '__main__':
    i=0
    for record in combinerecoverSecret():
        i+=1
        print record
    print str(i) + "records printed"
