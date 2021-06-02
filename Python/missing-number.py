from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Return the only number in the range that is missing from the array."""
        # SOLUTION 1
        # -- Submission Stats (as of June 1, 2021) --
        # Time Complexity: O(n)
        # Runtime: 124ms, faster than 88.53%
        # Space Complexity: O(1)
        # Memory Usage: 15.4 MB, less than 48.98%

        length = len(nums)
        return length * (length + 1) // 2 - sum(nums)


        # SOLTUION 2
        # -- Submission Stats (as of June 1, 2021) --
        # Time Complexity: O(n)
        # Runtime: 132ms, faster than 59.21%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 49.29%

        # return (set(range(len(nums)+1)) - set(nums)).pop()


        # SOLUTION 3
        # -- Submission Stats (as of June 1, 2021) --
        # Time Complexity: O(n)
        # Runtime: 184ms, faster than 17.53%
        # Space Complexity: O(1)
        # Memory Usage: 15.3 MB, less than 94.32%

        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing ^= i ^ num
        # return missing


        # SOLUTION 4
        # -- Submission Stats (as of June 1, 2021) --
        # Time Complexity: O(n)
        # Runtime: 2308 ms, faster than 12.94%
        # Space Complexity: O(1)
        # Memory Usage: 15.4 MB, less than 78.34%

        # nums.sort()
        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i

