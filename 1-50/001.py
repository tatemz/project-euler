# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Terms:
# * Natural number - A natural number is a number that occurs commonly and obviously in nature. As such, it is a whole, non-negative number. The set of natural numbers, denoted N, can be defined in either of two ways: N = {0, 1, 2, 3, ...}

ans = 0
for x in xrange(1,1000):
  divisibleByThree = True if (x % 3) == 0 else False
  divisibleByFive = True if (x % 5) == 0 else False
  if divisibleByThree or divisibleByFive:
    ans = ans + x
    if divisibleByThree:
      print "%s is divisible by 3 - new sum is %s" % (x, ans)
    if divisibleByFive:
      print "%s is divisible by 5 - new sum is %s" % (x, ans)

