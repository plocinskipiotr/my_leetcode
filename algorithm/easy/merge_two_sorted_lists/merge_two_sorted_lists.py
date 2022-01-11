from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ' ' + str(self.next)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        a = list1
        b = list2
        c = ListNode()
        head = c
        while a is not None and b is not None:

            if a.val < b.val:
                c.next = ListNode(a.val)
                a = a.next
            else:
                c.next = ListNode(b.val)
                b = b.next

            c = c.next

        if a is None:
            c.next = b

        if b is None:
            c.next = a

        return head.next
