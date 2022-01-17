from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        i = j = head
        while j is not None:
            if j.val != i.val:
                i.next = j
                i = j
            j = j.next

        if j != i:
           i.next = None
        return head
