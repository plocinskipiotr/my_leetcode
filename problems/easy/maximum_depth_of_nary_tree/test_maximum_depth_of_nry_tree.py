from unittest import TestCase
from maximum_depth_of_nry_tree import Solution, Node


class TestSolution(TestCase):
    def test_max_depth(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        root.children[1].children = None
        root.children[2].children = None
        lvl = s.maxDepth(root)
        self.assertEqual(3, lvl)

    def test_max_depth_recc(self):
        s = Solution()
        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        root.children[1].children = None
        root.children[2].children = None
        lvl = s.maxDepthRecursion(root)
        self.assertEqual(3, lvl)
