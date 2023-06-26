from unittest import TestCase
from intersection_of_two_linked_lists import Solution, ListNode


class TestSolution(TestCase):
    def test_get_intersection_node(self):
        s = Solution()
        l = ListNode('a1')
        l.next = ListNode('a2')
        r = ListNode('b1')
        r.next = ListNode('b2')
        r.next.next = ListNode('b3')
        c = ListNode('c1')
        l.next.next = c
        r.next.next.next = c
        c.next = ListNode('c2')
        c.next.next = ListNode('c3')
        x = s.getIntersectionNode(l, r)
        self.assertEqual(x, c)
