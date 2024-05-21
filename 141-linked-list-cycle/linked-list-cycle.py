class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = set()
        while head:
            if head in a:
                return True
            a.add(head)
            head = head.next
        return False