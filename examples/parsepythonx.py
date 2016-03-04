# parsepython.py
#
# Takes a filepath as input, 
# yields a python file for each solution.

import os, re, sys, time
sys.path.insert(0, '/home/joshuamcquiston/Documents/code-eval')
from recordsDict import records_dict
from itertools import izip

def parse_pythonx(solutionsfile):
    solutionsfile = open(solutionsfile, "r")
    skip = 0
    fi = open('p_solution.py', 'w')
    for line in solutionsfile:
        if skip:
            skip -= 1
            continue
        elif "Best Practices" in line:
            skip = 3
            try:
                with open('p_solution.py', 'r') as fi:
                    yield fi
                os.remove('p_solution.py')
                fi = open('p_solution.py','w')
            except Exception:
                continue
        else:
            fi.write(line)



# Example use

if __name__ == '__main__':
    solution = parse_pythonx(sys.argv[1])
    records = records_dict(sys.argv[1])
    i = 0
    for pair in izip(solution, records):
        i += 1
        os.system("clear")
        os.system("cat p_solution.py")
        print "\n"*3
        for label, record in pair[1].items():
        	print label, record
        time.sleep(.3)
        if raw_input() == 'exit':
        	break
    print str(i) + "records printed"

