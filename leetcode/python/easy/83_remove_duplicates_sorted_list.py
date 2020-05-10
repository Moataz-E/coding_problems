"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.
"""

class ListNode(object):
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def to_listnode(A):
        """Converts a list to a ListNode."""
        head = ListNode(A[0])
        current = head
        for i in range(1, len(A)):
            nxt = ListNode(A[i])
            current.next = nxt
            current = nxt
        return head

    @staticmethod
    def from_listnode(head):
        """Converts a ListNode to a list."""
        A = []
        current = head
        while current.next != None:
            A.append(current.val)
            current = current.next
        A.append(current.val)
        return A

class RemoveDuplicates:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Removes duplicates from a singly-linked list.

        Leetcode stats:
            Runtime: 72ms
            Memory Usage: 12.9MB

        Args:
            Head of a ListNode.

        Returns:
            ListNode with duplicates removed.
        """
        if head == None:
            return []

        while (head.next != None) and (head.val == head.next.val):
            head = head.next

        prev = head
        current = head.next
        while (current != None) and (current.next != None):
            if current.val == current.next.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return ListNode.from_listnode(head)


A = [3,6,12,14,14,18,21,21,27]
head = ListNode.to_listnode(A)
rd = RemoveDuplicates()
B = rd.deleteDuplicates(head)
assert(B == [3,6,12,14,18,21,27])

A = [1,1,2,3,3]
head = ListNode.to_listnode(A)
rd = RemoveDuplicates()
B = rd.deleteDuplicates(head)
assert(B == [1,2,3])

A = [1,1,1]
head = ListNode.to_listnode(A)
rd = RemoveDuplicates()
B = rd.deleteDuplicates(head)
assert(B == [1])

A = [1,3,6,7,7,7,12]
head = ListNode.to_listnode(A)
rd = RemoveDuplicates()
B = rd.deleteDuplicates(head)
assert(B == [1,3,6,7,12])
print(B)
