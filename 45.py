#Problem 45
'''
Triangle, pentagonal, and hexagonal numbers are generated
by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
t(n) = p(a)
(n**2 + n)/2 = 3/2a**2 - a/2


t(n) = h(b)
(n**2 + n)/2 = 2b**2 - b
'''
import math

#returning false because answer is 165.0002527
def matchtp(n):
    c = (n**2 + n) / 2
    if ((1/2)**2 - 4 * 3/2 * (-c)) > 0:
        if (1/2 + math.sqrt(1 - 4 * 3/2 * (-c)))/(2 * 3/2) % 1 == 0 or (1/2 - math.sqrt(1 - 4 * 3/2 * (-c)))/(2 * 3/2) % 1 == 0: return True
        else: return False
    else: return False
print(matchtp(285))


def matchth(n):
    c = n**2 + n
    if ((2)**2 - 4 * 4 * (-c)) > 0:
        if (2 + math.sqrt((2)**2 - 4 * 4 * (-c)))/(2 * 4) % 1 == 0 or (2 - math.sqrt((2)**2 - 4 * 4 * (-c)))/(2 * 4) % 1 == 0: return True
    else: return False

print(matchth(285))
def matchsmart(n):
    if matchtp(n) and matchth(n): return t(n)
    else: matchsmart(n+1)

#print(matchsmart(2))

def t(n):
    return n * (n + 1) / 2

def p(n):
    return n * (3 * n - 1) / 2
             
def h(n):
    return n * (2 * n - 1)

def match(n):
    n = n
    a = n
    #decrement a and b while p, h > t
    while (t(n) != p(a) or t(n) > p(a)) and a > 165:
        a -= 1
    if t(n) == p(a):
        b = a
        while (t(n) != h(b) or t(n) > h(b)) and b > 143:
            b -= 1
    if t(n) == p(a) == h(b):
        return t(n), n, a, b
    else: return match(n+1)


#print(match(285))
'''
print(triangonal(20) == pentagonal(12) == hexagonal(10))
print(triangonal(20))
print(pentagonal(12))
print(hexagonal(10))
'''
#print(triangonal(285) == pentagonal(165) == hexagonal(143), triangonal(285))
#print(match(2) == 40755, match(2))
