"""
function to double a number with recursion
"""

def double(n):
    if n == 0:
        return 0
    return double(n-1) + 2

print double(50)



#function to get factorial using recursion

def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n

print fact(12)


#function to get fibonacci number

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1

    else: return fib(n-1) + fib(n-2)

print fib(12)




#find sum of all list nums using recursion
def listsum(l):
    if len(l) == 0:
        return 0
    return listsum(l[1:]) + l[0]
print listsum([0,0,0,0])


#find sum of first n numbers

def sumfirstn(n):
    if n == 0: return 0
    return sumfirstn(n-1) + n
print sumfirstn(4)


#find sum of digits with recursion ofcourse
def sumdigits(n):
    if n <= 0 : return 0
    return sumdigits(n/10) + (n%10)
print sumdigits(1)


#convert a decimal number to base (2,8,10 etc) using recurdion
def convtobase(n, base):
    str_ = "0123456789ABCDEF"
    if n < base: return str_[n]
    return (convtobase(n//base, base)) + str_[n%base]
print convtobase(1433, 8)
print "****************"

def rev(l):
    if len(l) == 0:
        return
    rev(l[1:])
    res = []
    num = l[0]
    res.append(num)
    return res



l = [1,2,3]
print rev(l)