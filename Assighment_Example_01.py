largest = None
smallest = None

while True:
    num = input("enter the input : ")

    if num == "done":
        break

    try:
        num_int = int(num)

        if largest is None or num_int > largest:
            largest = num_int
        if smallest is None or num_int < smallest:
            smallest = num_int

    except ValueError:
        print('Invalid Number')

print("Largest:", largest)
print("Smallest:", smallest)
