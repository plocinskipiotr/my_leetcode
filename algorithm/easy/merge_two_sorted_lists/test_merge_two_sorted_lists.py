from unittest import TestCase

from merge_two_sorted_lists import Solution
from merge_two_sorted_lists import ListNode


class TestSolution(TestCase):
    def test_merge_two_lists_0(self):
        s = Solution()

        a = ListNode(4)
        a.next = ListNode(5)
        a.next.next = ListNode(6)

        b = ListNode(1)
        b.next = ListNode(2)
        b.next.next = ListNode(5)
        b.next.next.next = ListNode(7)

        x = s.mergeTwoLists(a, b)
        print(x)

    def test_merge_two_lists_1(self):
        s = Solution()

        a = ListNode(4)
        a.next = ListNode(5)
        a.next.next = ListNode(6)

        b = ListNode(1)

        x = s.mergeTwoLists(a, b)
        print(x)

    def test_merge_two_lists_2(self):
        s = Solution()

        a = ListNode(4)
        a.next = ListNode(5)
        a.next.next = ListNode(6)

        b = ListNode(7)

        x = s.mergeTwoLists(a, b)
        print(x)

    def test_merge_two_lists_3(self):
        s = Solution()

        a = None
        b = None

        x = s.mergeTwoLists(a, b)
        print(x)


    def test_merge_two_lists_4(self):
        s = Solution()

        a = ListNode(4)
        b = ListNode(2)

        x = s.mergeTwoLists(a, b)
        print(x)
