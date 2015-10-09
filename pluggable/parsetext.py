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

			

def parse_text1(solutions):
    
    for line in solutions:
		if 'same_structure_as' in line:
			try:
				yield file
			except Exception:
				pass
			file = open('sol.txt', 'w+')
			file.write(line)
		elif line == '\n':
			pass
		else:
			try:
				file.write(line)
			except Exception:
				pass
import re
def parse_text2(file_gen):
	#take a open file generator and yield open files
	import pdb;pdb.set_trace()
	for f in file_gen:
		#do something with an open file
		for line in f:
			if "Best Practices" in line:
				try:
					yield file
				except Exception:
					pass
				file = open('sol.txt','w+')
			elif re.match('def.*\(.*\):$', line):
				try:
					file.write(line)
				except Exception:
					pass
			else:
				pass


def parse_text3(file_gen):
	#take a open file generator and yield open files
	#import pdb;pdb.set_trace()
	import os, re
	for f in file_gen:
		#do something with an open file
		skip = 0
		fi = open('sol.txt', 'w')
		for line in f:
			if skip:
				skip -= 1
				continue
			elif "Best Practices" in line:
				skip = 3
				try:
					#import pdb;pdb.set_trace()
					fi = open('sol.txt', 'r')
					yield fi
					fi.close()
					os.remove('sol.txt')
					fi = open('sol.txt','w')
				except Exception:
				    continue
			else:
				fi.write(line)
						
  #this doesn't work, it is trying to do ALL of them!!
# Example use

if __name__ == '__main__':
	#import pdb; pdb.set_trace()
	from solutionsopen import solutions_open
	from solutionsfind import solutions_find
	solutions = solutions_find("*solutions.txt","solutions")
	solutionfiles = solutions_open(solutions)
	individuals = parse_text3(solutionfiles)
	for function in individuals:
		print '----------------------------'
		print function
		for line in function:
			print line

