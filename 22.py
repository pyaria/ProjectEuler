#Problem 22

'''Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''

#read names, put into a list and sort into alphabetical orderf

alph = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
        'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

def sortfile(f):
    a = open(f, 'r')
    b = (a.read().rsplit(","))
    c = []
    for name in b:
        c.append(name.strip('"'))
    return c
            
def subnamescore(name):
    subscore = 0
    for each in range(0,len(name)):
        subscore += alph[name[each]]
    return subscore

def filescore(filename):
    file = sortfile(filename)
    file.sort()
    score = 0
    for each in range(0,len(file)):
        score += subnamescore(file[each]) * (each + 1)
    return score

#print(filescore("P22names.txt"))


'''
print(len(sortfile("P22names.txt")))

print(filescore("P22names.txt"))
'''

print(filescore("P22names.txt"))
#print(subnamescore('COLIN'))
'''
print(sortfile('P22names.txt'))
'''
