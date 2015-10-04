# counthelpers.py
# 
# Count the number of helper functions in the solution.
# Takes a filename string as an input and yield a tuple with "helper functions" and a value.

import re, sys
sys.path.insert(0, '/home/josh/code-eval')
from parsetext import parse_text

def counthelpers(solutionsfile):
    for function in parse_text(solutionsfile):
    	function.seek(0)
    	helpers = []
        for line in function:
            for f in re.findall('(def.*\(.*\):)', line):
                helpers.append(f)
    	helpercount = len(helpers)-1
    	yield ('helpers', helpercount)


# Example use

if __name__ == '__main__':
	a = counthelpers("solutions.txt")
	for line in a:
		print line
