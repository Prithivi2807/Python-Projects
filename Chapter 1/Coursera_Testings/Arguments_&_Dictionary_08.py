def printDictionary(**args):
  for key in args:
    print(key + ":" + args[key])
  
printDictionary(Country='Canada', Province='Ontario', City='Toronto')
