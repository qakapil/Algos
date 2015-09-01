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
    if len(str1) + len(str2) != len(str3):
        return False

    if not str1 or not str2 or not str3:
        if str1 + str2 == str3:
            return True
        else:
            return False

    if str1[0] != str3[0] and str2[0] != str3[0]:
        return False



    if str1[0] == str3[0] and solution2_RECURSIVE(str1[1:], str2, str3[1:]):
        return True

    if str2[0] == str3[0] and solution2_RECURSIVE(str1, str2[1:], str3[1:]):
        return True

    return False





str1='abc'
str2='def'
str3='dabecf'

#print solution1(str1, str2, str3)
print solution2_RECURSIVE(str1, str2, str3)
