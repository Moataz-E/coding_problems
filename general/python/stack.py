class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.pop()
