#Problem 26

'''
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
'''

#find recurring cycle in decimal fraction
#b = digit to start at, set default at 2
def cycle(n, b):
    dec = str(n)
    test1 = ""
    if len(dec) > 5:
        for i in range(b, len(dec)-1):
            '''instead of dec[i] in test1, dec[i] in test1[0]'''
            if dec[i] not in test1:
                test1 += (dec[i])
            else: break
        if dec.find(test1, len(test1) + 2) > 0:
            #print (b)
            #print(test1)
            #print(len(dec))
            return len(test1)
        else: return cycle(n, b + 1)
    else: return len(dec) - b

def largestrecur(n):
    largestcycle = 1
    value = 2
    for i in range(2, n):
        challenge = cycle(1/i, 2)
        if challenge > largestcycle:
            value = i
            largestcycle = challenge
    return value

#print(cycle(1/3, 2))
#print(cycle(1/6, 2))
#print(cycle(1/8, 2))
#print(cycle(1/12, 2))
#print(cycle(1/3, 2) == 1, "cycle(1/3, 2)")
#print(cycle(1/7, 2) == 6, "cycle(1/7, 2)")
#print(largestrecur(10) == 7, "largestrecur(10)", largestrecur(10))
#print(largestrecur(1000))
#print(cycle(1/81, 2))
