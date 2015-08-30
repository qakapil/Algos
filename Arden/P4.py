"""
Find Missing Element
"""

def solution1(A,B):
    return sum(A)-sum(B)


def solution2(A,B):
    d = {}
    for num in B:
        if d.has_key(num):
            d[num] +=1
        else:
            d[num] = 0
    for num in A:
        if not d.has_key(num):
            return num
        if d[num] < 0:
            return num
        else:
            d[num] -= 1


def solution3(A,B):
    res = 0
    C = A+B
    for num in C:
        res = res^num
    return res


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [0, 1, 2, 3, 4, 6, 7, 8, 9]
print solution1(A,B)
print solution2(A,B)
print solution3(A,B)