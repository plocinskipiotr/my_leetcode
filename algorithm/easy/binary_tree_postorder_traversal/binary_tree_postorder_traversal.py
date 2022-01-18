from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root:
            result.extend(self.postorderTraversal(root.left))
            result.extend(self.postorderTraversal(root.right))
            result.append(root.val)
        return result

    def postorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = list(), deque()
        if root:
            el = root, '0'
        else:
            return []

        while stack or el[0]:
            if el[0] is None:
                el = stack.pop()
            if el[0] and el[1] == '0':
                stack.append((el[0], '1'))
                el = el[0].left, '0'
            elif el[0] and el[1] == '1':
                stack.append((el[0], '2'))
                el = el[0].right, '0'
            elif el[0] and el[1] == '2':
                result.append(el[0].val)
                el = None, '3'

        return result
