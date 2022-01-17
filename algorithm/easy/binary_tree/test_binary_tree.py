from unittest import TestCase

from binary_tree import TreeNode, Tree


class TestTree(TestCase):
    def test_insert_0(self):
        Tree0 = Tree(TreeNode(8))
        Tree0.insert(Tree0.root, TreeNode(3))
        Tree0.insert(Tree0.root, TreeNode(10))
        Tree0.insert(Tree0.root, TreeNode(1))
        Tree0.insert(Tree0.root, TreeNode(6))
        Tree0.insert(Tree0.root, TreeNode(14))
        Tree0.insert(Tree0.root, TreeNode(4))
        Tree0.insert(Tree0.root, TreeNode(7))
        Tree0.insert(Tree0.root, TreeNode(13))

        y = Tree0.traverse_in_order_stack(Tree0.root)
        self.assertEqual([1,3,4,6,7,8,10,13,14], y)
