

def dict_creator(solutionstextfile):  #if this takes a single solutions file, how will all the solution files get run?

sys.path.insert(0, '/home/josh/code-eval/pluggable')
#maybe python this out so that it is more portable.

   
    for pluggable in pluggable_find("pluggable")  #countlines, etc
        #maybe write a similar function to solutions_find but that will import the function instead and call it
        #import generat function in file
        #create an instance of the generator using the solutionsfile as input, 
        #add that instance to a list that will have next() called on each generator

        genlist.append(pluggable(solutionstextfile))  #pluggable needs to be the callable name of generatorfunction
        
        #while true, for each generator in list, create a dict call each next() 
        for gen in genlist:

        		gen(solutionstextfile)
        plug_gen = #call the function with  with solutions.txt
        next = plug_gen.next()
        dict[next[0]] = next[1]

    for solution in solutions:
        solutiondict = {}
        for pluggin in pluggins:


        yield solutiongedict  #one dictionary for each solution?
        



def pluggablefind()  #generator function that yields function files like countforloops.py and other user generated ones.