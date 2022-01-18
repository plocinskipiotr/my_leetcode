from unittest import TestCase
from remove_linked_list_elements import Solution, ListNode


class TestSolution(TestCase):
    def test_remove_elements(self):
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(5)
        head.next.next.next.next.next.next = ListNode(6)
        h = s.removeElements(head, 6)

        head = ListNode(7)
        head.next = ListNode(7)
        head.next.next = ListNode(7)
        h = s.removeElements(head, 7)
