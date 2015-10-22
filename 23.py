#Problem 23
'''
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if
the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number,
1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written
as the sum of two abundant numbers is 24.
By mathematical analysis,
it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot
be written as the sum of two abundant numbers.
'''
#check numbers up to 28123; all n >28123 == abundant
#find all abundant numbers up to 28123, put in list
#check if each number <28123 can be made by a sum of two abundant numbers

import math

def findfactors(n):
    factors = 0
    for i in range(1, int(math.sqrt(n)) + 1 ):
        if i == math.sqrt(n): factors += i
        elif n % i == 0: factors += i + n // i
    return factors - n

def isabundant(n):
    return findfactors(n) > n

def final(n):
    lst = []
    nonabunsum = 0
    for i in range(0, n+1):
        if isabundant(i): lst.append(i)
    for i in range(0, n+1):
        flag = True
        for a in lst:
            if i - a in lst:
                flag = False
                break
        if flag == True: nonabunsum += i
    return nonabunsum

print(final(28123))


'''
#return list of abundant numbers
def listabundant(n):
    listabun = []
    for i in range(0, n + 1):
        if isabundant(i): listabun.append(i)
    #print(listabun)
    return listabun

#return BOOL for if n is sum of two abundant numbers
def chksumabundant(n):
    flag = False
    listabun = listabundant(n)
    for i in listabun:
        if n % i == 0 and n // i in listabun:
            flag = True
            break
    return flag

#if n < 28123 is not sum of two abundant numbers, sum
def notabundantsum(n):
    final = 0
    for m in listabun:
        if m - n in listabun: break
        else:
            final += m
    return final

def final(n):
    lstabun = []
    lstabun.extend(listabundant(n))
    fin = 0
    for num in range(0, n+1, 2):
        flag = True
        for a in lstabun:
            if num - a in lstabun:
                flag = False
                break
        if flag == True: fin += num
    return fin
        
#print(final(28123))

def odd(n):
    final = 0
    for i in range(0, n, 2):
        final += i
    return final

def oddabund(n):
    odds = 0
    for i in listabundant(n):
        if i % 2 != 0: odds += i
    return odds

print(oddabund(28123))

#print(odd(28123)+final(28123)-oddabund(28123))
#not 197726048
'''
'''
print(findfactors(28) == 28, "findfactors(28)", findfactors(28))
print(findfactors(12) == 16, "findfactors(12)", findfactors(12))
print(isabundant(12) == True, "Is 12 abundant")
print(isabundant(28) == False, "Is 28 abundant")
'''
