# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, p: TreeNode | None, q: TreeNode | None):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lvl = [root] if root else None

        while lvl:
            lst = list()
            for el in lvl:
                if el is None:
                    continue
                lst.append(el.right)
                lst.append(el.left)

            i = 0
            j = len(lst) - 1
            while i < j:
                if not self.check(lst[i], lst[j]): return False
                i += 1
                j -= 1

            lvl = lst

        return True
