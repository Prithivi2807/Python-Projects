# BMI = WEIGHT / (height) ** 2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# write your code below this line

bmi = float(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)