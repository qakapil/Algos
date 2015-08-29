__author__ = 'kapil'

def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


print(anagramSolution1('abcd','dcba'))


def anagramSolution2(s1,s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))


print(anagramSolution2('acdb','dcba'))


def anagramSolution3(s1,s2):
    #bruteforce
    pass


def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1
    stillOK = True
    j = 0
    while j < 26 and stillOK:
        if c1[j] != c2[j]:
            stillOK = False
        else:
            j += 1
    return stillOK
print(anagramSolution4('delhi','dehli'))