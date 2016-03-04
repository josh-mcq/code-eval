# parsetext.py
#
# Takes a filepath as input,
# yields a text file for each solution.

import os, re, sys, time

def parse_text(solutionsfile):
	solutionsfile = open(solutionsfile, "r")
	skip = 0
	fi = open('t_solution.txt', 'w')
	for line in solutionsfile:
		if skip:
			skip -= 1
			continue
		elif "Best Practices" in line:
			skip = 3
			try:
				with open('t_solution.txt', 'r') as fi:
					yield fi
				os.remove('t_solution.txt')
				fi = open('t_solution.txt','w')
			except Exception:
			    continue
		else:
			fi.write(line)

  
# Example use


if __name__ == '__main__':
    result = parse_text(sys.argv[1])
    i = 0
    for line in result:
        i+=1
        print line
        time.sleep(.03)
    print str(i) + "records printed"
