import os

class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, k):
        self.heap_list.append(k)
        self.size += 1
        self._percolate_up(self.size)

    def find_max():
        pass

    def pop_max():
        pass

    def is_empty():
        pass

    def size():
        pass

    def build_heap():
        pass

    def _percolate_up(self, i):
        while (i // 2) > 0:
            if self.heap_list[i//2] < self.heap_list[i]:
                parent = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = parent
            i =// 2

    def _percolate_down(self):
        while (i * 2) < self.size:
            if self.heap_list[i*2] >= self.heap_list[i]:
                mc_index = self._max_child(i)
                mc = self.heap_list[mc_index]
                self.heap_list[mc_index] = self.heap_list[i]
                self.heap_list[i] = mc
            i = mc_index

    def _max_child(self, i):
        if (i*2 + 1) > self.size:
            return 1 * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i*2 + 1]:
                return i * 2
            else:
                return i*2 + 1
