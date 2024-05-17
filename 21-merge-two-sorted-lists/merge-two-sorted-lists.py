# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        o = ListNode()
        t = o
        while list1 and list2:
            if list1.val < list2.val:
                o.next = list1
                list1 = list1.next
            else:
                o.next = list2
                list2 = list2.next
            o = o.next
        if list1:
            o.next = list1
        if list2:
            o.next = list2
        return t.next


