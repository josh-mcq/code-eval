# counthelpers.py
# 
# Count the number of helper functions in the solution.
# Takes a filename string as an input and yield a tuple with "helper functions" and a value.

import re, sys
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
# Must be called from code-eval/

if __name__ == '__main__':
    a = counthelpers("solutions/" + sys.argv[1] + "/solutions.txt")
    i=0
    for line in a:
        i+=1
        print line
    print str(i) + "records printed"

