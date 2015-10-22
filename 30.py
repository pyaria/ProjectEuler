#Problem 30

def power(num, pow):
    s = str(num)
    b = []
    for a in s:
        b.append(int(a)**pow)
    if sum(b) == num: return num
    else: return False

def test(pow):
    b = []
    a = 2
    while a < 10**(pow-1):
        s = str(a)
        c = []
        for d in s:
            c.append(int(d)**pow)
        if sum(c) == a:
            b.append(a)
            a += 1
        else: a += 1
    return b


#print(power(1634, 4))
#print(power(8208, 4))
#print(power(9474, 4))
#print(power(1111, 4))


print(test(4))
