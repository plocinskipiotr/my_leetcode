# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst: list[int]):
        if len(lst) == 0:
            return ListNode(-1)

        x = [ListNode(x) for x in lst]
        for i in range(len(x[:-1])):
            x[i].next = x[i + 1]

        return x[0]

    def to_int_list(self) -> list[int] | None:
        x = self

        int_lst = []
        while x is not None:
            if x.val > 0:
                int_lst.append(x.val)
            x = x.next

        return int_lst


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = ListNode()
        head = curr

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1

        return head.next
