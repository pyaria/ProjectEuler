#Problem 36
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''

#returns BOOL 
def ispalindrome(n):
    n = str(n)
    return n == n[::-1]

#print(ispalindrome(5885))

def sumpalindromes(n):
    b = 0
    for i in range(1, n):
        a = bin(i).lstrip("0b")
        if a[0] != "0" and str(i)[0] != "0" and ispalindrome(i) and ispalindrome(a): b += i
    return b

print(sumpalindromes(1000000))

