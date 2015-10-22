#Problem 15

'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def factorial(n):
   b = n
   for a in range(1, n): b *= a
   return b

#print(factorial(3))

def pathlength(n):
   return int(factorial(n + n)/(factorial(n) * factorial(n)))

print(pathlength(2))
print(pathlength(20))
