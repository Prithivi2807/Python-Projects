def is_palindrome(x):
  x = str(x)
  return x == x[::-1]

x=input("Enter the words/number you want to convert into a string ?")
print(is_palindrome(x))