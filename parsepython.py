# parsepython.py
#
# Takes a solutions_open generator as input, 
# yields a python file for each solution.


def parse_python(solutionsfile):
	#take a solutions file and yield individual solution open files
	#import pdb;pdb.set_trace()
	import os, re
	#for f in file_gen:
		#do something with an open file
	solutionsfile = open(solutionsfile, "r")
	skip = 0
	fi = open('solz.py', 'w')
	for line in solutionsfile:
		if skip:
			skip -= 1
			continue
		elif "Best Practices" in line:
			skip = 3
			try:
				#import pdb;pdb.set_trace()
				#fi = open('sol.txt', 'r')
				#yield fi
				#fi.close()
				with open('solz.py', 'r') as fi:
					yield fi
				os.remove('solz.py')
				fi = open('solz.py','w')
			except Exception:
			    continue
		else:
			fi.write(line)