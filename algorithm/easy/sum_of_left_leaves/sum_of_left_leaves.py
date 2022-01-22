from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        suma = 0

        if root is None:
            return 0

        if root.right:
            suma += self.sumOfLeftLeaves(root.right)

        if root.left:
            if root.left.left is None and root.left.right is None:
                return suma + root.left.val

        if root.left:
            suma += self.sumOfLeftLeaves(root.left)

        return suma

    def sumOfLeftLeavesIter(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        suma = 0
        while q:
            el = q.popleft()
            if el.left:
                if el.left.left is None and el.left.right is None:
                    suma += el.left.val

                q.append(el.left)

            if el.right:
                q.append(el.right)

        return suma