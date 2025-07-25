class Solution(object):
  def is_palindrome(self, x):
    if x < 0:
      return False
    if x == 0:
      return True
    if x % 10 == 0: # ex: 30 is not a palindrome
      return False
    
    originalX = x
    numReversed = 0
    while x > 0:
      lastDigit = x % 10
      numReversed = numReversed * 10 + lastDigit
      x = x // 10
    
    return numReversed == originalX
  
  