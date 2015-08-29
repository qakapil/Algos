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

def parChecker(symbolString):
    """
    (()()()())
    (((())))
    (()((())()))
    """
    index = 0
    balanced = True
    s = Stack()
    while index < len(symbolString) and balanced:
        if symbolString[index] == '(':
            s.push('(')
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))






def parChecker2(symbolString):
    index = 0
    balanced = True
    s = Stack()
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                pop_symb = s.pop()
                if not matches(pop_symb, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    openers = "[{("
    closers = "]})"
    return openers.index(open) == closers.index(close)



print(parChecker2('{{([)[])}()}'))
print(parChecker2('[{()]'))



