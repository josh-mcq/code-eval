def combine(*args):  
  #import pdb; pdb.set_trace()
  result = []
  args = list(args)
  print len(args)
  if len(args) < 2:
    return []
  i = 0
  lfunc = lambda x: len(x)
  longest = sorted(args, key=lfunc, reverse=True)[0]
  while i < len(longest):
      for arg in args:
        try:
          result.append(arg[i])
        except IndexError:
             pass
    
      i+=1
  return result