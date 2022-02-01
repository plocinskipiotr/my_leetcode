from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root: Optional[TreeNode]):

        if root:
            h_l, h_r = 0, 0
            if root.left:
                h_l = self.traverseTree(root.left) + 1
            if root.right:
                h_r = self.traverseTree(root.right) + 1
            h = max(h_l, h_r)
            diameter = h_l + h_r
            self.max_high = diameter if diameter > self.max_high else self.max_high
            return h

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_high = 0
        self.traverseTree(root)
        return self.max_high
