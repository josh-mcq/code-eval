# countseconds.py
# 
# Count the number of seconds it takes to run the testcases.
# Takes a filename string as an input and yield a tuple with "runtime" and a value.

#from parsetext import parse_text

def countseconds(solutionsfile):
	from parsetext import parse_text
	for function in parse_python(solutionsfile):
		testcases = gettestcases(solutionsfile)
		runtime = 
		yield ('runtime', runtime)


# Example use

if __name__ == '__main__':
	import sys
	sys.path.insert(0, '/home/josh/code-eval')
	from parsetext import parse_text
	a = countlines("solutions.txt")
	for line in a:
		print line
