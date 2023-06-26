from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            lst = [root.val]
            if root.children:
                for child in root.children:
                    lst.extend(self.preorder(child))
        else:
            return []
        return lst

    def preorder_iter(self, root: 'Node') -> List[int]:
        if not root:
            return []
        deq = deque([root])

        lst = list()
        while len(deq):
            el = deq.pop()
            lst.append(el.val)
            if el.children is not None:
                deq.extend(el.children[::-1])
        return lst
