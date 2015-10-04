# countlines.py
# 
# Count the number of lines in the solution.
# Takes a filename string as an input and yield a tuple with "linecount" and a value.

#from parsetext import parse_text

def countlines(solutionsfile):
	from parsetext import parse_text
	for function in parse_text(solutionsfile):
		function.seek(0)
		yield ('line count', len(function.readlines()))


# Example use

if __name__ == '__main__':
	import sys
	sys.path.insert(0, '/home/josh/code-eval')
	from parsetext import parse_text
	a = countlines("solutions.txt")
	for line in a:
		print line
