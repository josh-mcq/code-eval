# countseconds.py
# 
# Count the number of seconds it takes to run the testcases.
# Takes a filename string as an input and yield a tuple with "runtime" and a value.


import sys, random
sys.path.insert(0, '/home/joshuamcquiston/Documents/code-eval')
from parsepython import parse_python
import os
import datetime, time
import unittest



def countseconds(solutionsfile):
    testcase_path = ("/").join(solutionsfile.split("/")[:-1])+"/testcases.txt"
    for func in parse_python(solutionsfile):
		os.system("cat " + testcase_path + " >> p_solution.py")
		start = datetime.datetime.now()
		tmp = unittest.main(module = "p_solution", exit = False)
		end = datetime.datetime.now()
		duration = end - start
		yield ('seconds', duration.total_seconds())



# Example use

if __name__ == '__main__':
	rand_dir = random.choice(["recoverSecret","whoIsNext","same_structure_as", "rgb"])
	path = "solutions/" + "combine" + "/solutions.txt"
	result = countseconds(path)
	i = 0
	for line in result:
		i+=1
		print line
		time.sleep(.03)
	print path
	print str(i) + "records printed"