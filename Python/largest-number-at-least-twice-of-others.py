from typing import *


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        '''Return the index of the largest element iff largest element is at least twice as much as all other numbers in array.'''

        # Runtime: 31 ms
        # Memory: 14.1 MB
        maxVal = max(nums)
        maxIndex = nums.index(maxVal)
        count = 0

        for e in nums:
            if e != maxVal and e*2 <= maxVal:
                count += 1

        if count == len(nums) - 1:
            return maxIndex
        return -1

        # --- OLD SOLUTION ---?
        # Runtime: 36 ms
        # Memory: 14 MB

        # if len(nums) == 1:
        #     return 0

        # maxVal = nums.index(max(nums))
        # nums.sort()

        # return maxVal if (nums[-2]*2 <= nums[-1]) else -1


a = Solution()
print(a.dominantIndex([3, 6, 1, 0]))
