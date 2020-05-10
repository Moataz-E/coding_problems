class Node:
    """Represents a node in a linked list."""

    def __init__(self, data):
        self.next = None;
        self.data = data;
        

    def append_to_tail(self, data):
        """Appends a new node to the 
