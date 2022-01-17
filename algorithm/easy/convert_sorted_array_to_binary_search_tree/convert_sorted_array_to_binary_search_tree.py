from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:

        l, r = 0, len(nums) - 1
        i = (l + r) // 2
        node = TreeNode(nums[i])
        stack = [(l, i - 1, node, 'l'),
                 (i + 1, r, node, 'r')]

        while stack:
            l, r, parent, side = stack.pop()

            if l <= r:
                i = (l + r) // 2

                child = TreeNode(nums[i])
                if side == 'l':
                    parent.left = child
                else:
                    parent.right = child

                stack.append((l, i - 1, child, 'l'))
                stack.append((i + 1, r, child, 'r'))

        return node
