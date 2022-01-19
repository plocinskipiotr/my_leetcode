# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTreeIter(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return
        deck = deque([root])

        while deck:
            node = deck.popleft()
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                deck.extend([node.left, node.right])
        return root