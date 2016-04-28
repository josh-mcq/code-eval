# combineAll
#
# Takes no parameters currently


from analyze import *
from itertools import izip
import sys

def combine_molecules_to_atoms():
	lines = countlines.countlines("solutions/molecules_to_atoms/solutions.txt")
	ifs = countifstatements.countifstatements("solutions/molecules_to_atoms/solutions.txt")
	helpers = counthelpers.counthelpers("solutions/molecules_to_atoms/solutions.txt")
	fors = countforloops.countforloops("solutions/molecules_to_atoms/solutions.txt")
	seconds = countseconds.countseconds("solutions/molecules_to_atoms/solutions.txt")
	allrecords = izip(lines,ifs,helpers,fors,seconds)
	return allrecords

def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True

# Example use
# Must be called from code-eval/


if __name__ == '__main__':
    i=0
    for record in combine_molecules_to_atoms():
        i+=1
        print record
    print str(i) + "records printed"
