from unittest import TestCase
from reverse_linked_list import Solution, ListNode


class TestSolution(TestCase):
    def test_reverse_list(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        d = s.reverseList(head)

    def test_reverse_list2(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        d = s.reverseList(head)

    def test_reverse_list3(self):
        s = Solution()
        head = ListNode(1)
        d = s.reverseList(head)

    def test_reverse_list4(self):
        s = Solution()
        head = None
        d = s.reverseList(head)

    def test_reverse_recc_list(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        d = s.reverseListRecursive(head)
        print("xD")

    def test_reverse_recc_list2(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        d = s.reverseListRecursive(head)
        print("xD")

    def test_reverse_recc_list3(self):
        s = Solution()
        head = ListNode(1)
        d = s.reverseListRecursive(head)
        print("xD")

    def test_reverse_recc_list4(self):
        s = Solution()
        head = None
        d = s.reverseListRecursive(head)
        print("xD")