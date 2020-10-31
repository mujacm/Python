#Count number of ways to reach nth stair, adobe product internship assessment question on 30th October'2020
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Returns no. of ways to
# reach sth stair
def countWays(s):
    return fib(s + 1)

# Driver program
s = 4
print "Number of ways = ",
print countWays(s)
