# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root, path, lst_path) -> List[str]:

        if root:

            path = str(root.val) if not path else path + "->" + str(root.val)

            if not root.right and not root.left:
                lst_path.append(path)

            self.traverse(root.left, path, lst_path)
            self.traverse(root.right, path, lst_path)

            return lst_path

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.traverse(root, '', [])

    def binaryTreePathsIter(self, root: Optional[TreeNode]) -> List[str]:
        deck = deque([(root, '')])
        lst_path = []
        while deck:
            el, path = deck.popleft()
            if not el:
                continue

            if not path:
                path = str(el.val)
            else:
                path = path + '->' + str(el.val)

            deck.extend([(el.left, path), (el.right, path)])
            if not el.left and not el.right:
                lst_path.append(path)

        return lst_path
