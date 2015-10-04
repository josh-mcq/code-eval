# countforloops.py
# 
# Count the number of for loops in the solution.
# Takes a filename string as an input and yield a tuple with "linecount" and a value.

import re, sys
sys.path.insert(0, '/home/josh/code-eval')
from parsetext import parse_text

def countforloops(solutionsfile):
    for function in parse_text(solutionsfile):
    	function.seek(0)
    	loops = []
        for line in function:
            for f in re.findall('(for.*in )', line):
                loops.append(f)
    	loopcount = len(loops)
    	yield ('for loop count', loopcount)


# Example use

if __name__ == '__main__':
	a = countforloops("solutions.txt")
	for line in a:
		print line
