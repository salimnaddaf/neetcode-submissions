# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        r1=head
        r2=head.next
        while r1.next!=None:
            if r1 and r2 and r1.val==r2.val:
                return True
            r1=r1.next
            if r2.next is not None:
                r2=r2.next.next
        return False