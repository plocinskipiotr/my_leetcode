from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bt_h(node: TreeNode):
            if not node:
                return 0

            l_h = bt_h(node.left)
            r_h = bt_h(node.right)
            if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            return 1 + max(l_h, r_h)

        return bt_h(root) != -1
