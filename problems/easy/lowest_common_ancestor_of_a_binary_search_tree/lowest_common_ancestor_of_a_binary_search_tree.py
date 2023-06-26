# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

    def lowestCommonAncestorreccurence(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorreccurence(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorreccurence(root.left, p, q)
        else:
            return root
