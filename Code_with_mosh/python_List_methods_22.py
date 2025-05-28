numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(0, 10) #0 is the index position, 10 is the value add in the list
print(numbers)
numbers.remove(20)  # remove thte value
print(numbers)
numbers.clear() # empties the list
print(numbers)
numbers = [5, 2, 1, 7, 4]
numbers.pop() # it removes the last item
print(numbers) 
numbers = [5, 2, 1, 7, 4] # use this number to find the index numbers
print(numbers.index(4)) 
print(50 in numbers) # in operator boolean value we will get false
print(numbers.count(5))
numbers=[5, 2, 1, 7, 4]
print(f"The actual numbers {numbers}")
numbers.sort() # sort the numbers in ascending order
print(f"ascending order numbers {numbers}")

numbers=[5, 2, 1, 7, 4]
print(f"Descending order numbers {numbers}") # numbers in reverse order

numbers2= numbers.copy()
numbers.append(10)
print(numbers2)