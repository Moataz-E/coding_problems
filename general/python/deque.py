class Deque:

    def __init__(self):
        self.items = []

    def pushFront(self, item):
        self.items.insert(0, item)

    def pushRear(self, item):
        self.items.append(item)

    def popFront(self):
        item = self.items[0]
        del self.items[0]
        return item

    def popRear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()
d.pushFront(1)
d.pushRear(3)
d.pushRear(5)
d.popFront()
d.popFront()
d.popRear()
d.popRear()
