from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0

        deq = deque([root])
        lst = []
        lvl_cnt = 0

        while len(deq) > 0:
            el = deq.popleft()
            if el and el.children is not None:
                for e in el.children:
                    lst.append(e)

            if len(deq) == 0:
                deq.extend(lst)
                lst.clear()
                lvl_cnt += 1

        return lvl_cnt

    # def traversedfs(self, root: 'Node', h: int) -> int:
    #     if root.children is not None:
    #         for node in root.children:
    #             self.traversedfs(node, h + 1)
    #     self.max_high = h if h > self.max_high else self.max_high
    #     return self.max_high
    #
    # def maxDepthRecursion(self, root: 'Node') -> int:
    #     if not root:
    #         return 0
    #     self.max_high = 0
    #     self.max_high = self.traversedfs(root, 0)
    #     return self.max_high + 1

    def maxDepthRecursion(self, root: 'Node') -> int:
        if not root:
            return 0
        else:
            h = 0
            print('root: ', root.val, ' h: ', h)
            if root.children:
                for node in root.children:
                    h = max(h, self.maxDepthRecursion(node))
                    print('h_max: ', h)
        return h + 1
