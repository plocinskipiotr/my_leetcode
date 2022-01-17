# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        lst: list[TreeNode | None] = list()
        lvl = 1

        while True:
            while queue:
                lst.append(queue.pop())

            for node in lst:
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(node)

            lst.clear()

            if not any(queue):
                return lvl
            lvl += 1

    def maxDepth0(self, root: Optional[TreeNode]) -> int:

        depth = 0
        lvl = [root] if root else []
        while lvl:
            depth += 1
            queue = []
            for el in lvl:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            lvl = queue
        return depth
