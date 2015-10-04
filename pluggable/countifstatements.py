# countifstatements.py
# 
# Count the number of if-statements in the solution.
# Takes a filename string as an input and yield a tuple with "if statements" and a value.

import re, sys
sys.path.insert(0, '/home/josh/code-eval')
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

if __name__ == '__main__':
	a = countifstatements("solutions.txt")
	for line in a:
		print line
