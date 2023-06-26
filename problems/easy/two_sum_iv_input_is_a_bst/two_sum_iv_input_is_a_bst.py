from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root: Optional[TreeNode], k: int):

        if root:
            for item in self.d:
                if root.val + item == k:
                    return True

            self.d.add(root.val)
            bool = self.traverseTree(root.left, k)
            if bool:
                return True
            bool = self.traverseTree(root.right, k)
            return bool

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d = set()
        x = self.traverseTree(root, k)
        return x

    def traverseTree2(self, main_root: TreeNode, root: Optional[TreeNode], myset: set, k: int):

        if root:
            diff = k - root.val
            if diff in myset:
                return True
            myset.add(diff)
            x = self.binary_search(main_root, root, diff)

            if x:
                return True

            b = self.traverseTree2(main_root, root.left, myset, k)
            a = self.traverseTree2(main_root, root.right, myset, k)

            if a or b:
                return True

    def binary_search(self, main_root: TreeNode, root: TreeNode, target: int):
        if main_root:
            if main_root != root and main_root.val == target:
                return True
            elif main_root.val > target:
                return self.binary_search(main_root.left, root, target)
            elif main_root.val < target:
                return self.binary_search(main_root.right, root, target)

    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        return self.traverseTree2(root, root, set(), k)
