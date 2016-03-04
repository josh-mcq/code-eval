#parsetestcase
#
# Takes a solution directory name and yields a single testcase, one at a time(as what?..
# to be used in addtestcases, and changes from # codewars(Test.assert_equals..  to self.assertEquals) to unittest name
# oh shit, there may be other ones besides assert_equals too..   maybe just create a dictionary?



def parse_testcase(solutions_dir):
    #take a testcases file and yield individual 
	#import pdb;pdb.set_trace()
	import os, re
	#for f in file_gen:
		#do something with an open file
	tests_path = "solutions/" + solutions_dir + "testcases.txt"
	testfile = open(tests_path, "r")
	skip = 0
	fi = open('test.txt', 'w')
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
			fi.write(line)  #not creating a file here, most likely a list.