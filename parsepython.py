# parsepython.py
#
# Takes a filepath as input, 
# yields a python file for each solution.
import os, re, sys, time
def parse_python(solutionsfile):
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
    result = parse_python(sys.argv[1])
    i = 0
    w = 3
    for line in result:
        i+=1
        os.system("clear")
        os.system("cat p_solution.py")
        time.sleep(.3)
        if raw_input() == 'exit':
        	break
    print str(i) + "records printed"
