# parsetext.py
#
# Takes a solutions_open generator as input,
# yields a text file for each solution.


def parse_text(solutionsfile):
	#take a solutions file and yield individual solution open files
	#import pdb;pdb.set_trace()
	import os, re
	#for f in file_gen:
		#do something with an open file
	solutionsfile = open(solutionsfile, "r")
	skip = 0
	fi = open('sol.txt', 'w')
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
				with open('sol.txt', 'r') as fi:
					yield fi
				os.remove('sol.txt')
				fi = open('sol.txt','w')
			except Exception:
			    continue
		else:
			fi.write(line)


  
# Example use

if __name__ == '__main__':
	#import pdb; pdb.set_trace()
	from solutionsopen import solutions_open
	from solutionsfind import solutions_find
	solutionsfile = "solutions.txt"
	for function in parse_text(solutionsfile):
		for line in function:
			print line

