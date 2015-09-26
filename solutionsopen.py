# solutionsopen.py
#
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been open


def solutions_open(filenames):
    for name in filenames:
        if name.endswith(".txt"):
            yield open(name)

# Example use

if __name__ == '__main__':
    from solutionsfind import  solutions_find
    solutions = solutions_find("*solutions.txt","solutions")
    solutionfiles = solutions_open(solutions)
    for s in solutionfiles:
        print s
