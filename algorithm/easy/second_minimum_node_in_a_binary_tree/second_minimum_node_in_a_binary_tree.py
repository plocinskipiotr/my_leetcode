# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverseTree(self, root: TreeNode, min1):
        if root:

            if min1 < root.val < self.ans:
                self.ans = root.val
            else:
                self.traverseTree(root.left, min1)
                self.traverseTree(root.right, min1)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.traverseTree(root, root.val)

        return self.ans if self.ans < float('inf') else -1
