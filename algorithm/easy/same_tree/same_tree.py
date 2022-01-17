from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def check(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = Queue()
        que.put((p, q))

        while not que.empty():
            node_p, node_q = que.get()
            if not self.check(node_p, node_q):
                return False

            if node_p:
                que.put((node_p.left, node_q.left))
                que.put((node_p.right, node_q.right))

        return True
