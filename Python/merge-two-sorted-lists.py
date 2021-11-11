# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = []
        while l1 or l2:
            if l1:
                q.append(l1)
                l1 = l1.next
            if l2:
                q.append(l2)
                l2 = l2.next
        q.sort(key=lambda x: x.val)
        for i in range(len(q)-1):
            q[i].next = q[i+1]
        return q[0] if len(q) else None
