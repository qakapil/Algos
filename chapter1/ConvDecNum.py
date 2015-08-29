class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def divideBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        rem = decNumber%2
        decNumber = decNumber//2
        s.push(rem)
    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())

    return binString

print(divideBy2(42444))


def baseConverter(decNumber, base):
    s = Stack()
    nums = "0123456789ABCDEF"
    while decNumber > 0:
        rem = decNumber%base
        s.push(rem)
        decNumber = decNumber//base
    resultString = ''
    while not s.isEmpty():
        resultString += str(nums[s.pop()])
    return resultString

print(baseConverter(2577,2))
print(baseConverter(2577,16))
