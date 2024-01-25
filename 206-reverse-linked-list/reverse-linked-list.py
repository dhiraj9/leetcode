# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        t = head
        while t:
            a.append(t.val)
            t = t.next
        t = head
        while t:
            t.val = a.pop()
            t = t.next
        return head



