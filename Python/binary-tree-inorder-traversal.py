from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # OLD SOLUTION
        # -- Submission Stats (as of May 17, 2021) --
        # Time Complexity: O(n)
        # Runtime: 24ms, faster than 94.51%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 12.23%
        # if root == None:
        #     return []
        # else:
        #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # NEW SOLUTION

