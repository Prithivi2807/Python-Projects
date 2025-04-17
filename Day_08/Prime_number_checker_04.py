# Write your code belwo
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print(f"It's not a prime number. it is divisible by {i-1}")


# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)

