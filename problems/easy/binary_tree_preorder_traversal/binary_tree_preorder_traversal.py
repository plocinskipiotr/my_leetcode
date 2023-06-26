from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root:
            result.append(root.val)
            result.extend(self.preorderTraversal(root.left))
            result.extend(self.preorderTraversal(root.right))
        return result

    def preorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = list(), deque()
        if root:
            el = root
        else:
            return []

        while stack or el:
            if el:
                result.append(el.val)
                stack.append(el)
                el = el.left
            if el is None and stack:
                el = stack.pop()
                el = el.right
        return result
