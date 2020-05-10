"""
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class KSmallestBST:

    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """Find kth smallest element in Binary Search Tree.

        Leetcode stats:
            Runtime: 68ms
            Memory Usage: 17.5MB

        Args:
            root: TreeNode root of BST.
            k: int representing rank of smallest element we want to find.

        Returns:
            Integer representing kth smallest element in BST.
        """
        flat_bst = []
        self.flatten_bst(root, flat_bst)
        flat_bst.sort()
        return flat_bst[k-1]

    def flatten_bst(self, root, flat_bst):
        if root == None:
            return

        flat_bst.append(root.val)
        self.flatten_bst(root.left, flat_bst)
        self.flatten_bst(root.right, flat_bst)

# Generate Sample Tree
n1 = TreeNode(1)
n1.right = TreeNode(2)
root = TreeNode(3)
root.left = n1
root.right = TreeNode(4)

kbst = KSmallestBST()
flat_bst = []
kbst.flatten_bst(root, flat_bst)
assert(kbst.kth_smallest(root, 1) == 1)
