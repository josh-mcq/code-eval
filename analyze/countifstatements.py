# countifstatements.py
# 
# Count the number of if-statements in the solution.
# Takes a filename string as an input and yield a tuple with "if statements" and a value.

import re, sys
from parsetext import parse_text

def countifstatements(solutionsfile):
    for function in parse_text(solutionsfile):
    	function.seek(0)
    	ifs = []
        for line in function:
            for f in re.findall('(if.*:)', line):
                ifs.append(f)
    	ifcount = len(ifs)
    	yield ('if statements', ifcount)


# Example use
# Must be called from code-eval/

if __name__ == '__main__':
    a = countifstatements("solutions/" + sys.argv[1] + "/solutions.txt")
    i = 0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"
