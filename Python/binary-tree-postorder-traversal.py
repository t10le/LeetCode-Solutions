from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """Returns the postorder traversal of the given root of a binary tree"""

        # OLD SOLUTION
        # -- Submission Stats (as of May 17, 2021) --
        # Time Complexity: O(n)
        # Runtime: 32ms, faster than 52.90%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 46.72%

        # base case
#         if root == None:
#             return []

#         # recursive case
#         else:
#             return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]



        # NEW SOLUTION
        # -- Submission Stats (as of May 17, 2021) --
        # Time Complexity: O(n)
        # Runtime: 24ms, faster than 94.37%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 46.72%
        if root == None:
            return []
        result, stack, visited = [], [root], {root}
        while stack:
            node = stack[-1]
            skip = True

            if node.right and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)
                skip = False
            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.add(node.left)
                skip = False
            if skip:
                result.append(node.val)
                stack.pop()

        return result


