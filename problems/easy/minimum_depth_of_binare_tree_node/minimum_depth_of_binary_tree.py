# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, lvl = q.popleft()
            if node:
                if not node.right and not node.left:
                    return lvl
                else:
                    q.append((node.left, lvl + 1))
                    q.append((node.right, lvl + 1))

    def minDepth_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left:
            return self.minDepth_dfs(root.right) + 1
        elif not root.right:
            return self.minDepth_dfs(root.left) + 1
        else:
            return min(self.minDepth_dfs(root.left), self.minDepth_dfs(root.right)) + 1
