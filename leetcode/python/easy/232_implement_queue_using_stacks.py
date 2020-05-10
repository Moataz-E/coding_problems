"""
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:
1. You must use only standard operations of a stack -- which means only push
    to top, peek/pop from top, size, and is empty operations are valid.
2. Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.
3. You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
"""
class StackQueue(object):

    def __init__(self):
        """Initialize two lists which we will use as two stacks.

        Leetcode stats:
            Runtime: 36ms
            Memory Usage: 13.1MB

        We treat the last element in the list as the top of the stack.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """Push element x to the back of queue.

        Args:
            x: int to be pushed into queue.
        """
        if len(self.stack1) < 1:
            self.stack1.append(x)
        else:
            self.stack2.append(x)

    def pop(self) -> int:
        """Removes the element from front of queue and returns that element.

        Returns:
            element in front of queue.
        """
        item_to_return = self.stack1.pop()
        if self.stack2:
            while len(self.stack2) > 1:
                self.stack1.append(self.stack2.pop())
            new_top = self.stack2.pop()
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(new_top)
        return item_to_return

    def peek(self) -> int:
        """Get the front element.

        Returns:
            front element in queue.
        """

        return self.stack1[0]

    def empty(self) -> bool:
        """Returns whether the queue is empty.

        Returns:
            bool representing whether queue is empty or not.
        """
        return True if len(self.stack1) == 0 else False

sq = StackQueue()
sq.push(1)
sq.push(2)
sq.push(3)
sq.push(4)
assert(sq.peek() == 1)
assert(sq.pop() == 1)
assert(sq.empty() == False)
