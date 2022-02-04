from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mapTree(self, root: Optional[TreeNode], subtree: Optional[list[int]] = None) -> list[int | None]:
        if not root:
            return [None]
        if root:
            map = list()
            map.extend(self.mapTree(root.left, subtree))
            map.extend(self.mapTree(root.right, subtree))
            map.append(root.val)
            if subtree is not None and map == subtree:
                self.has_subtree = True
            return map

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.has_subtree = False
        subtree = self.mapTree(subRoot)
        self.mapTree(root, subtree)
        return self.has_subtree
