# countlines.py
# 
# Count the number of lines in the solution.
# Takes a filename string as an input and yield a tuple with "linecount" and a value.

import sys
from parsetext import parse_text


def countlines(solutionsfile):
    #import pdb; pdb.set_trace()
    for function in parse_text(solutionsfile):
		function.seek(0)
		yield ('line count', len(function.readlines()))


# Example use
# Must be called from code-eval/

if __name__ == '__main__':
    a = countlines("solutions/" + sys.argv[1] + "/solutions.txt")
    i = 0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"
