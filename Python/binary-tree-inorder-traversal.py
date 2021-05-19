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

        # ALTERNATIVE SOLUTION
        # -- Submission Stats (as of May 17, 2021) --
        # Time Complexity: O(n)
        # Runtime: 28ms, faster than 80.67%
        # Space Complexity: O(n)
        # Memory Usage: 14 MB, less than 98.49%

        stack, result, visited = [root], [], {root}
        if root == None:
            return []

        while stack:
            node = stack.pop()
            skip = True

            if node.right and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)
                skip = False

            stack.append(node)

            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.add(node.left)
                skip = False

            if skip:
                result.append(stack.pop().val)

        return result

