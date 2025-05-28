# Given an integer x, return True if x 
# is a palindrom and False otherwise
  
class Solution:
  def isPalindrome(self, x:int):
    if x < 0 and x % 10 ==0 :
      return False
    if x == 0:
      return True
    
    originalX = x
    num_Rev = 0 
    while x > 0:
      last_digit = x % 10
      num_Rev = num_Rev * 10 + last_digit
      x = x // 10
    return num_Rev == originalX
  
x = int(input("Enter the number: "))

sol = Solution()
print("is Palindrome ?", sol.isPalindrome(x))