from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        i = dummy

        while i:
            while i.next and i.next.val == val:
                i.next = i.next.next
            i = i.next
        return dummy.next
