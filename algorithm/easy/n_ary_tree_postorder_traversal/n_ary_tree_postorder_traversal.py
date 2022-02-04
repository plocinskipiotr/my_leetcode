from typing import List
from collections import deque


# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            lst = list()
            if root.children:
                for child in root.children:
                    lst.extend(self.postorder(child))

            lst.append(root.val)
            return lst

    def postorder_iter(self, root: 'Node') -> List[int]:
        if not root:
            return []

        deq = deque()
        deq.append(root)
        lst = list()
        while deq:
            el = deq.pop()
            if isinstance(el, Node):
                deq.append((el, 'VISITED'))
                if el.children is not None:
                    deq.extend(el.children[::-1])
            else:
                lst.append(el[0].val)
        return lst
