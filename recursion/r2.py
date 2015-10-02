"""
factorial with recursion
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print factorial(10)



def explode(word):
    if len(word) < 1:
        return word
    return word[0]+ ' '+ explode(word[1:])

print explode('hello')+'1'


def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])

print removeDups('')+'1'


#function to double a number with recursion
def doubleNum(n):
    if n <= 0:
        return 0
    return 2 + doubleNum(n-1)
print doubleNum(1.5)


#function to get fibonacci number
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1

    else: return fib(n-1) + fib(n-2)

print fib(12)


#find sum of all list nums using recursion
def listsum(l):
    if len(l) <= 0:
        return 0
    return l[0] + listsum(l[1:])

print listsum([])


#find sum of first n numbers

def sumfirstn(n):
    if n == 0:
        return 0
    return n + sumfirstn(n-1)

print sumfirstn(4)


#find sum of digits with recursion ofcourse
def sumdigits(n):
    if n <= 0 : return 0
    return sumdigits(n/10) + (n%10)
print sumdigits(1)