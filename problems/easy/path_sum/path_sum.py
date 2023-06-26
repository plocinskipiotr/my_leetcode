from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        que = deque()
        if root is None:
            return False

        que.append((root, targetSum))
        while que:
            node, node_sum = que.popleft()
            if node:
                if node.left is None and node.right is None and node.val == node_sum:
                    return True
                que.append((node.left, node_sum - node.val))
                que.append((node.right, node_sum - node.val))
        return False
