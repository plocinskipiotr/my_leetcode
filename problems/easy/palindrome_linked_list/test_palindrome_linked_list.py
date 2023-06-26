from unittest import TestCase
from palindrome_linked_list import ListNode,Solution

class TestSolution(TestCase):
    def test_is_palindrome(self):
        s = Solution()
        n = ListNode(1)
        n.next = ListNode(5)
        n.next.next = ListNode(6)
        n.next.next.next = ListNode(6)
        n.next.next.next.next = ListNode(5)
        n.next.next.next.next.next = ListNode(1)
        x = s.isPalindrome(n)
        self.assertTrue(x)

    def test_is_palindrome2(self):
        s = Solution()
        n = ListNode(1)
        n.next = ListNode(2)
        n.next.next = ListNode(2)
        n.next.next.next = ListNode(1)
        x = s.isPalindrome(n)
        self.assertTrue(x)


