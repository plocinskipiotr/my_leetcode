from unittest import TestCase
from n_ary_tree_postorder_traversal import Solution, Node


class TestSolution(TestCase):
    def test_postorder(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        x = s.postorder(root)
        print(x)

    def test_postorder_iter(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        x = s.postorder(root)
        print(x)
