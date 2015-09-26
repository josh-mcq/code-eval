# parsetext.py
#
# Takes a solutions_open generator as input,
# yields a text file for each solution.

def parse_text(solutions):
    
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
	

  
# Example use

if __name__ == '__main__':
	import pdb; pdb.set_trace()
	from solutionsopen import solutions_open
	from solutionsfind import solutions_find
	solutions = solutions_find("*solutions.txt","solutions")
	solutionfiles = solutions_open(solutions)
	individuals = parse_text(solutionfiles)
	for x in individuals:
		x.seek(0)
		x.read()
