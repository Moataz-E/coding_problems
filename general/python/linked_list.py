class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.get_value() == item:
                next_node = current.get_next()
                if previous == None:
                    self.head = next_node
                else:
                    previous.set_next(next_node)
            else:
                previous = current
                current = current.get_next()

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_value() == item:
                return True
            current = current.get_next()
        return False

    def is_empty(self):
        return self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def append(self, item):
        """Adds element at the end of the list."""
        current = self.head
        previous = None
        while current != None:
            previous = current
        new_node = Node(item)
        previous.set_next(new_node)
        new_node.set_next(None)

    def index(self, item):
        """Returns index of the item in the list."""
        current = self.head
        count = 0
        while current.get_value() != item:
            count += 1
        return count

    def insert(self, pos, item):
        """Inserts item at exactly that position in the list"""
        pass

    def pop(self):
        """Removes and returns last element in the list."""
        pass

    def pop(self, pos):
        """Removes and returns element at specific location in the list."""
        pass
