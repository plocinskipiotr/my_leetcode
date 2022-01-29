from collections import Counter
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root: Optional[TreeNode]) -> Counter:
        c = Counter()

        if not root:
            return c

        c.update([root.val])
        c.update(self.traverseTree(root.left))
        c.update(self.traverseTree(root.right))

        return c

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = self.traverseTree(root)
        most_popular_value = max(c.values())
        return [x[0] for x in c.items() if x[1] == most_popular_value]
