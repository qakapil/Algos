"""
Transform One String to Another using Minimum Number of Given Operation
Input:  A = "ABD", B = "BAD"
Output: 1
Explanation: Pick B and insert it at front.

Input:  A = "EACBD", B = "EABCD"
Output: 3
Explanation: Pick B and insert at front, EACBD => BEACD
             Pick A and insert at front, BEACD => ABECD
             Pick E and insert at front, ABECD => EABCD
"""


def solution(A, B):
    m = len(A)
    n = len(B)
    if m != n:
        return -1
    cnt = [0]*256
    for ch in A:
        pos = ord(ch)
        cnt[pos] += 1
    for ch in B:
        pos = ord(ch)
        cnt[pos] -= 1
    for i in range(256):
        if cnt[i] != 0:
            return -1

    i = j = n-1
    res = 0
    while (i >= 0):
        if A[i] != B[j]:
            res += 1
            i -= 1
        elif i >= 0:
            i -= 1
            j -= 1
    return 'the number of steps are %d' % res



A = 'CAAA'
B = 'AAAC'

print solution(A,B)