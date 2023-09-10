# Define the Hello function
def Hello(a, b):
    return a + b


try:
    # Get user input for two numbers separated by a space
    input_str = input("Enter two numbers separated by a space: ")

    # Split the input string into a list of two strings
    input_list = input_str.split()

    # Check if there are exactly two elements in the list
    if len(input_list) != 2:
        raise ValueError("Please enter two numbers separated by a space.")

    # Convert the input strings to floating-point numbers
    num1 = float(input_list[0])
    num2 = float(input_list[1])

    # Call the Hello function with the user input
    result = Hello(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")
except ValueError as e:
    print(f"Invalid input: {e}")
