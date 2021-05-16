from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """preorder = root, left, right"""

        # Time Complexity:  O(N) + O(N) = O(n)
        # Space Complexity: O(n)
        # base case
        #if root == None:
        #    return []
        # general case
        #else:
        #    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)



        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
