fruits = ["Apple", "Pear", "Orange"]

#TODO : Catch the exception and make sure the code will run properly
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else: 
    print(fruit + " pie")
    