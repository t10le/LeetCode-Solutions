# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return it as a sorted list. The list should be made by 
        splicing together the nodes of the first two lists.
        """

        # -- Submission Stats (as of Nov 11, 2021) --
        # Time Complexity: O(n)
        # Runtime: 24ms, faster than 99.77%
        # Space Complexity: O(n)
        # Memory Usage: 14.4 MB, less than 32.14%

        backlog = []
        while l1 or l2:
            if l1:
                backlog.append(l1)
                l1 = l1.next
            if l2:
                backlog.append(l2)
                l2 = l2.next

        if backlog == []:
            return l1

        backlog = sorted(backlog, key=lambda x: x.val)

        for i in range(len(backlog)-1):
            backlog[i].next = backlog[i+1]

        return backlog[0]

        # --- Test ---
        # b = ListNode(1, None)
        # a = ListNode(0, b)
        # return a
        # Output --> [0, 1]
