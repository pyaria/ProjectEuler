#Problem 17

d = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
     "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
     "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
     "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
     "19": "nineteen", "20": "twenty", "30": "thirty",
     "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy",
     "80": "eighty", "90": "ninety", "100": "hundred", 
     "1000": "onethousand"}

def count1(n):
    #n < 10
    ltr_ct = 0
    for number in range(1, n+1): ltr_ct += len(d[str(number)])
    return ltr_ct

def count99(n):
    #n>20, n<100
    ltr_ct = 0
    ltr_ct += count1(19)
    snum = str(n)
    if n > 19:
        ltr_ct += len(d[snum[0] + "0"]) * (int(snum[-1]) + 1)
        n -= 10
        while n > 19:
            dumn = str(n)
            ltr_ct += len(d[dumn[0] + "0"]) * 10
            n -= 10
    if snum[-1] == "0":
        ltr_ct += count1(9) * (int(snum[0]) - 2)
    else:
        ltr_ct += count1(int(snum[-1])) * (int(snum[0]) - 1)
        if n > 30:
            ltr_ct += count1(9) * (int(snum[0]) - 2)
    return ltr_ct

def count199(n):
    ltr_ct = 0
    snum = str(n)
    inum = int(snum[1:3])
    if inum < 21 : ltr_ct += count1(inum) + 3 * (inum)
    else: ltr_ct += count99(inum) + 3 * (inum)
    inum = int(snum[0])
    ltr_ct += count99(99) * inum
    ltr_ct += (len(d[snum[0]]) + len(d["100"])) * (int(snum[1:3]) + 1)
    return ltr_ct

def count999(n):
    ltr_ct = 0
    snum = str(n)
    inum = int(snum[1:3])
    if inum < 20 : ltr_ct += count1(inum) + 3 * (inum)
    else : ltr_ct += count99(inum) + 3 * (inum)
    hun = int(snum[0])
    ltr_ct += (len(d[str(hun)]) + len(d["100"])) * (inum + 1)
    hun -= 1
    while hun > 1:
        ltr_ct += (len(d[str(hun)]) + len(d["100"])) * 100
        ltr_ct += count99(99) + 3 * 99
        hun -= 1
    ltr_ct += count199(199)
    return ltr_ct

def count(n):
    ltr_ct = 0
    if n < 21 : ltr_ct += count1(n)
    elif n < 100 : ltr_ct += count99(n)
    elif n < 200 : ltr_ct += count199(n)
    elif n < 1000 : ltr_ct += count999(n)
    else:
        ltr_ct += len(d["1000"]) + count999(999)
    return ltr_ct

'''
print (count(5) == 19, "1")
print (count(10) == 39, "2")
print (count(19) == 106, "3")
print (count(20) == 112, "4")
print (count(29) == 202, "5")
print (count(30) == 208, "6")
print (count(39) == 298, "7")
print (count(40) == 303, "8")
print (count(49) == 384, "9")
print (count(50) == 389, "10")
print (count(99) == 854, "11")
print (count(100) == 864, "12")
print (count(101) == 880, "13")
print (count(110) == 1033, "14")
print (count(199) == 3005, "15")
print (count(200) == 3015, "16")
print (count(201) == 3031, "17")
print (count(220) == 3387, "18")
print (count(299) == 5156, "20")
print (count(300) == 5168, "21")
print (count(399) == 7507, "22")
print (count(1000))
'''
