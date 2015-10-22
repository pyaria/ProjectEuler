#Problem 13
'''Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.'''

def readnumber(n):
    file = open(n, "r")
    fsum = 0
    for line in file:
        fsum += int(line)
        print(line)
    return str(fsum)[0:10]


print(readnumber("P13numbers.txt"))
