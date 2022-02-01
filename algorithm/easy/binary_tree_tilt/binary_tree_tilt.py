from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[1]

    def traverse(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if root is None:
            return 0, 0

        left_sum, left_diff = self.traverse(root.left)
        right_sum, right_diff = self.traverse(root.right)
        suma = root.val + left_sum + right_sum
        diff = left_diff + right_diff + abs(left_sum - right_sum)
        return (suma, diff)
