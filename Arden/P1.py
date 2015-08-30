"""
Given an integer array, output all pairs that sum up to a specific value k.
"""

def solution1(A,S):
    res = []
    for i in xrange(len(A)):
        for j in xrange(i+1, len(A)):
            if (A[i]+A[j] == S):
                res.append((A[i],A[j]))
    return res


def solution2(A,S):
    res = []
    if len(A) < 2:
        return False
    A.sort()
    left, right = (0, len(A)-1)
    while left < right:
        currentSum = A[left]+A[right]
        if currentSum == S:
            res.append((A[left],A[right]))
            left += 1
        elif currentSum < S:
            left += 1
        else:
            right -= 1
    return res


def solution3(A,S):
    if len(A) < 2:
        return False
    seen = set()
    output = set()
    for num in A:
        target = S-num
        if target in seen:
            output.add((target,num))
        else:
            seen.add(num)
    return str(output)



def solution4(A, S):
    res = []
    diff_hash = {}
    for i in A:
        if diff_hash.has_key(i):
            res.append((i, diff_hash[i]))
        key = S - i
        diff_hash[key] = i
    return res

A = [0,4,1,9,10,2,6,0,10]
S = 10

print solution1(A, S)
print solution2(A, S)
print solution3(A, S)
print solution4(A, S)

