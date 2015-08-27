class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def hotPotato(namelist, num):
    simque = Queue()
    for name in namelist:
        simque.enqueue(name)

    while simque.size() > 1:
        for i in range(num):
            simque.enqueue(simque.dequeue())
        simque.dequeue()

    return simque.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
