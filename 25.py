#Problem 25
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
#1, 1, 2, 3, 5, 8, 13, 21, 34

#create Fibonnaci sequence
def Fibonnaci(n):
    a = 2
    b = 3
    term = 4
    fib = 5
    for i in range(0,n-4):
        fib = a + b
        a = b
        b = fib
        term += 1
    return fib

def Fibonnaciterm(n):
    a = 2
    b = 3
    term = 4
    fib = 5
    while len(str(fib)) != n:
        fib = a + b
        a = b
        b = fib
        term += 1
    return term

        
print(Fibonnaci(11) == 89, "Fibonnaci(11)", Fibonnaci(11))
print(Fibonnaci(12) == 144, "Fibonnaci(12)", Fibonnaci(12))
print(Fibonnaci(10) == 55, "Fibonnaci(10)", Fibonnaci(10))
print(Fibonnaciterm(3) == 12, "Fibonnaci(3)", Fibonnaciterm(3))
print(Fibonnaciterm(1000))
