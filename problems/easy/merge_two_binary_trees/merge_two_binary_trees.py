# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root2:
            return root1
        if not root1:
            return root2

        deq = deque([(root1, root2)])

        while len(deq) > 0:
            a, b = deq.pop()

            b.val += a.val

            if a.left and b.left:
                deq.append((a.left, b.left))

            if a.right and b.right:
                deq.append((a.right, b.right))

            if a.left is not None and b.left is None:
                b.left = a.left

            if a.right is not None and b.right is None:
                b.right = a.right

        return root2

    def mergeTreesReccur(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTreesReccur(root1.left, root2.left)
        root1.right = self.mergeTreesReccur(root1.right, root2.right)
        return root1
