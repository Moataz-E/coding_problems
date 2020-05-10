"""
Given the root of a binary search tree with distinct values, modify it so that
every node has a new value equal to the sum of the values of the original tree
that are greater than or equal to node.val.
"""
import copy
from typing import List
from collections import deque
from bisect import bisect_left


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class BstToGst:

    def bin_tree_to_list(self, root: TreeNode) -> List[int]:
        nodes_queue = deque([root])
        tree_list = []
        tree_list.append(root.val)
        while len(nodes_queue) > 0:
            curr = nodes_queue.popleft()
            if curr.left is None:
                tree_list.append(None)
            else:
                nodes_queue.append(curr.left)
                tree_list.append(curr.left.val)
            if curr.right is None:
                tree_list.append(None)
            else:
                nodes_queue.append(curr.right)
                tree_list.append(curr.right.val)
        # Remove trailing None
        while True:
            if tree_list[-1] is not None:
                break
            tree_list.pop()
        return tree_list

    @staticmethod
    def list_to_tree(tree_list):
        root = TreeNode(tree_list[0])
        counter = 0
        nodes = deque([root])
        while counter <= (len(tree_list) - 2) // 2:
            next_left = 2 * counter + 1
            next_right = 2 * counter + 2
            curr = nodes.popleft()
            if tree_list[next_left] is None:
                curr.left = None
            else:
                curr.left = TreeNode(tree_list[next_left])
                nodes.append(curr.left)
            if tree_list[next_right] is None:
                curr.right = None
            else:
                curr.right = TreeNode(tree_list[next_right])
                nodes.append(curr.right)
            counter += 1
        return root

    def list_to_gst(self, tree_list: List[int], root: TreeNode) -> TreeNode:
        nodes_queue = deque([root])
        while len(nodes_queue) > 0:
            curr = nodes_queue.popleft()
            gt = bisect_left(tree_list, curr.val)
            new_val = sum(tree_list[gt:])
            curr.val = new_val
            if curr.left:
                nodes_queue.append(curr.left)
            if curr.right:
                nodes_queue.append(curr.right)
        return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return []
        # Convert binary tree to list
        tree_list = self.bin_tree_to_list(root)
        # sort list and remove None types
        tree_list = sorted([v for v in tree_list if v])
        # create copy of binary tree
        new_tree = copy.deepcopy(root)
        # traverse copy and replace with sum of bisect on sorted list
        new_tree = self.list_to_gst(tree_list, new_tree)
        # return copy of binary tree
        return self.bin_tree_to_list(new_tree)

btg = BstToGst()
inpt = btg.list_to_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
expected_out = [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
assert(expected_out == btg.convertBST(inpt))
