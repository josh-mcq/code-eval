# countseconds.py
# 
# Count the number of seconds it takes to run the testcases.
# Takes a filename string as an input and yield a tuple with "runtime" and a value.

#from parsetext import parse_text
import sys, random
sys.path.insert(0, '/home/joshuamcquiston/Documents/code-eval')
from parsepython import parse_python
import os
import datetime, time
import unittest



def countseconds(solutionsfile):
    #import pdb;pdb.set_trace()
    testcase_path = ("/").join(solutionsfile.split("/")[:-1])+"/testcases.txt"
    #testcase_path = "/solutions/recoverSecret/testcases.txt"
    for func in parse_python(solutionsfile):
		#func is a python file with one solution
		os.system("cat " + testcase_path + " >> p_solution.py")
		start = datetime.datetime.now()
		tmp = unittest.main(module = "p_solution", exit = False)
		end = datetime.datetime.now()
		duration = end - start
		yield ('tests-microseconds', duration.microseconds)



# Example use

if __name__ == '__main__':
	rand_dir = random.choice(["recoverSecret","whoIsNext","same_structure_as"])
	path = "solutions/" + "recoverSecret" + "/solutions.txt"
	result = countseconds(path)
	i = 0
	for line in result:
		i+=1
		print line
		time.sleep(.03)
	print path
	print "fyi: there are 1,000,000 microseconds in a second.."
	print str(i) + "records printed"