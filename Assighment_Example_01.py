largest = None
smallest = None
while True:
    num = input("Enter the input: ")
    if num == "done":
        break
    try:
        num_1 = int(num)
        if largest is None or num_1 > largest:
            largest = num_1
        if smallest is None or num_1 < smallest:
            smallest = num_1
    except:
        print('Invalid input')
print("largest", largest)
print("smallest", smallest)
