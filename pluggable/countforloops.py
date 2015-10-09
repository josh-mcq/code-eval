# countforloops.py
# 
# Count the number of for loops in the solution.
# Takes a filepath string as an input and yield a tuple with "linecount" and a value.

import re, sys
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
# Must be called from code-eval/


if __name__ == '__main__':
    a = countforloops("solutions/" + sys.argv[1] + "/solutions.txt")
    i = 0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"
