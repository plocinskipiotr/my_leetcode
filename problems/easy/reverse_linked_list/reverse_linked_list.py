# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def rev(self, n: Optional[ListNode], next: Optional[ListNode]):
        if next is None:
            return n

        prev = n
        n = next
        next = next.next
        n.next = prev
        return self.rev(n, next)

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = self.rev(None, head)
        return d