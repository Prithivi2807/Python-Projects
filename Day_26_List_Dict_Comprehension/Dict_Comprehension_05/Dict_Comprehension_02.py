sentence = "What is the Airspeed Velocity of an unladen Swallow?"
# Don't change code above

# write your code below:
sentence.split()
print(sentence)

result = {name:len(name) for name in sentence.split() }
print(result)

