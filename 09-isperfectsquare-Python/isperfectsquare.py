# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

from math import sqrt

def isperfectsquare(n):
  if type(n)==int and n>=0:
    return n == (sqrt(n)**2)
  elif (type(n)==int and  n<=0) or type(n)==float:
    return False
  elif n.isdigit():
    n=int(n)
    return n == (sqrt(n)**2)
  else:
    return False
