# countseconds.py
# 
# Count the number of seconds for the solution to pass the testcases.
# Takes a filename string as an input and yield a tuple with "linecount" and a value.

import sys
from parsetext import parse_text


def countseconds(solutionsfile):
	#what if modified the parameter to be "solutions" + solutionsfile + "solutions.txt"  where solutionsfile would actually be the name of the directory?
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
