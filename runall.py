# runall.py


def nested_gen(a, b):
    yield a
    yield b


def fakegen():
    x = 1
    while True:
        yield x
        x +=1

a = fakegen()
b = fakegen()
c = nested_gen(a, b)


# Example use

if __name__ == '__main__':
	#import pdb; pdb.set_trace()
	from solutionsopen import solutions_open
	from solutionsfind import solutions_find
	solutions = solutions_find("*solutions.txt","solutions")
	solutionfiles = solutions_open(solutions)
	individuals = parse_text(solutionfiles)
	for function in individuals:
		print '----------------------------'
		print function
		for line in function:
			print line

