weight = int(input("Enter the weight: \n"))
unit = input('(L)bs or (K)g: [n]').lower()

if unit == 'l':
    converted = weight ** 0.45 
    print(f"You are {converted} kilos")
elif unit == 'k':
    converted = weight / 0.45
    print(f"You are {converted} pounds" )