"""
Combine Two Strings
"""

def solution1(str1, str2, str3):
    ptr1 = ptr2 = 0
    stillOK = True
    for ptr3 in xrange(len(str3)):
        print str1[ptr1], str2[ptr2], str3[ptr3]
        if str3[ptr3] == str1[ptr1]:
            ptr1 += 1
        elif str3[ptr3] == str2[ptr2]:
            ptr2 += 1
        else:
            stillOK = False
            break

    return stillOK

def solution2_RECURSIVE(str1, str2, str3):
    pass #to be implemented after recursion chapter study



str1='abc'
str2='def'
str3='dabecf'

print solution1(str1, str2, str3)
