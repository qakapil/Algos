"""
how-to-convert-string-to-number-without-using-library-function
"""

def solution(s):
    res = 0
    for i in xrange(len(s)):
        res = res * 10 + ord(s[i]) - 48
    return res

s  = '12'

print solution(s)