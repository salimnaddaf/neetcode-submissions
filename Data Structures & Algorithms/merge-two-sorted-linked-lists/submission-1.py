# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        l1  = list1
        l2  = list2
        if l1.val > l2.val:
            runner=l2
            l2=l2.next
        else:
            runner=l1
            l1=l1.next
        head = runner
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                runner.next=l1
                l1=l1.next
            else:
                runner.next=l2
                l2=l2.next
            runner=runner.next
        if l1 is None:
            runner.next=l2
        if l2 is None:
            runner.next=l1
        return head
