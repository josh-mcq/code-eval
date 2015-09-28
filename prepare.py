if __name__ == '__main__':
	#import pdb; pdb.set_trace()
from parsetext import *
from solutionsopen import solutions_open
from solutionsfind import solutions_find
solutions = solutions_find("*solutions.txt","solutions")
solutionfiles = solutions_open(solutions)
individuals = parse_text3(solutionfiles)