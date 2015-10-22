#Problem 10
'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''

def isprime(n):
    prime = True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 : prime = False
    elif math.sqrt(n) % 1 == 0 : prime = False
    else:
        start = int(math.sqrt(n))
        if start % 2 == 0 : start -= 1
        while start > 9 :
            if n % start == 0 :
                prime = False
                break
            start -= 2
    return prime

def sumprime(n):
    add = 2 + 3 + 5 + 7
    if n % 2 == 0 : n -= 1
    while n > 10:
        if isprime(n):
            add += n
            n -= 2
        else : n -= 2
    return add

'''
print(isprime(5) == True, "5")
print(isprime(7) == True, "7")
print(isprime(11) == True, "11")
print(isprime(13) == True, "13")
print(isprime(9) == False, "9")
print(isprime(100) == False, "100")
'''

print(sumprime(10) == 17, "10")
print(sumprime(11) == 28, "11")
print(sumprime(2000000))
