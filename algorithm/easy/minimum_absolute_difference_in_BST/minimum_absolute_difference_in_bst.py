# Definition for a binary tree node.
from typing import Optional

MAX_VALUE = 9999999


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root) -> int:
        if root:
            self.traverse(root.left)
            self.diff = min(self.diff, abs(root.val - self.prev))
            self.prev = root.val
            self.traverse(root.right)

        return int(self.diff)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = int(MAX_VALUE)
        self.diff = int(MAX_VALUE)
        return self.traverse(root)
