import os

class Map:
    """Implementation of a hashmap that uses mid-square hash and chaining."""
    def __init__(self, map_size=20):
        """Initialize an empty map collection"""
        self.map_size = map_size
        self.keys = [None] * map_size
        self.values = [None] * map_size

    def put(self, key, value):
        """Add new key-value to map, if key exists then replace."""
        key_hash = self.hash(key)
        if self.keys[key_hash] == None:
            self.keys[key_hash] = [key]
            self.values[key_hash] = [value]
        else:
            self.keys[key_hash].append(key)
            self.values[key_hash].append(value)

    def get(self, key):
        """Given key, return value stored in Map."""
        key_hash = self.hash(key)
        if self.keys[key_hash] == None:
            return None
        else:
            if key not in self.keys[key_hash]:
                return None
            key_index = self.keys[key_hash].index(key)
            return self.values[key_hash][key_index]

    def delete(self, key):
        """Remove key and its value from Map."""
        key_hash = self.hash(key)
        if self.keys[key_hash] == None:
            return
        key_index = self.keys[key_hash].index(key)
        self.keys[key_hash].pop(key_index)
        self.values[key_hash].pop(key_index)

    def len(self):
        """Return number of key-value pairs stored in Map."""
        total_len = 0
        for i in range(self.map_size):
            total_len += len(self.keys[i])
        return total_len

    def is_in(self, key):
        """Return True if key is in our map."""
        for i in range(self.map_size):
            if key in self.keys[i]:
                return True
        return False

    def hash(self, key):
        """Compute hash using mid-square method."""
        square = pow(key, 2)
        square_string = str(square)
        len_ss = len(square_string)
        if len_ss < 3:
            return square % self.map_size
        else:
            return int(square_string[len_ss//2:(len_ss//2)+2]) % self.map_size

m = Map()
m.put(16, "Test")
m.put(242, "Time!")
m.get(14)
m.delete(16)
m.values
