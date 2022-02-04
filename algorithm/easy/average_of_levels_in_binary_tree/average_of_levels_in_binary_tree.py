from functools import reduce
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        deq = deque([root])

        lst = list()
        mean_lst = [root.val]
        suma = 0
        while len(deq):
            el = deq.pop()
            if el.left:
                lst.append(el.left)
                suma += el.left.val
            if el.right:
                lst.append(el.right)
                suma += el.right.val

            if len(deq) == 0:
                if len(lst):
                    mean_lst.append(suma / len(lst))
                deq.extend(lst)
                suma = 0
                lst.clear()
        return mean_lst

    def averageOfLevelsIter(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        lvl = 0
        deq = deque([(root, lvl)])
        d = {}

        while len(deq):
            el, lvl = deq.pop()

            if el is not None:

                if lvl in d.keys():
                    d[lvl].append(el.val)
                else:
                    d[lvl] = [el.val]

                deq.append((el.left, lvl + 1))
                deq.append((el.right, lvl + 1))

        return [reduce(lambda x, y: x + y, x[1]) / len(x[1]) for x in d.items()]
