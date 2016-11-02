import sys
print(sys.version)
import math
import time
'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
This program intends to find the value of the first triangle number to have over five hundred divisors.
'''
startTime = time.time() # Start timer

def getFactors(n):
    factors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            factors.extend([i, n/i])
    factors.sort()
    return factors

gotHighlyDivisible = False
triangular = 1
i = 2
factors = 1
while not gotHighlyDivisible:
    triangular = triangular + i
    factors = len(getFactors(triangular))
    if factors >= 5000:
        gotHighlyDivisible = True
        break
    i = i + 1

print("Highly divisible triangular is : " + str(triangular))
print("Time Required for execution : " + str(time.time()-startTime))
