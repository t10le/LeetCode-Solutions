from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """Returns the merged tree from root1 and root2 binary trees."""
        # -- Submission Stats (as of June 13, 2021) --
        # Time Complexity: O(n)
        # Runtime: 88ms, faster than 54.62%
        # Space Complexity: O(n)
        # Memory Usage: 15.4 MB, less than 48.03%
        
        # base case
        if root1 is None and root2 is None:
            return None
        
        # cond 2: one of the nodes are missing; assume root2 
        # if root1 is not None and root2 is None:
        # root1 = None, root2 = 7
        elif root1 is None:
            return TreeNode(root2.val, self.mergeTrees(root1, root2.left), self.mergeTrees(root1, root2.right))
            
        # cond 3: one of the nodes are missing
        # root1 = 5, root2 = None
        elif root2 is None:
            return TreeNode(root1.val, self.mergeTrees(root1.left, root2), self.mergeTrees(root1.right, root2))
        
        # cond 1: nodes overlap, so combine them together
        else:
            return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))
        
