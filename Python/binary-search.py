class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.
        """
        
        # if target in nums:
        #     return nums.index(target)
        # return -1
  
#         if nums != []:
#             midpoint = len(nums)//2
            
#             if target == nums[midpoint]:
#                 return midpoint
            
#             elif target > nums[midpoint]:
#                 return self.search(nums[midpoint+1:], target)
            
#             return self.search(nums[:midpoint], target)
#         return -1


        # SOLUTION
        # -- Submission Stats (as of Oct 15, 2021) --
        # Time Complexity: O(log(n))
        # Runtime: 239ms, faster than 63.51%
        # Space Complexity: O(1)
        # Memory Usage: 15.5 MB, less than 42.23%
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # avoids integer overflow
            midpoint = left + ((right-left) // 2) 
            if nums[midpoint] == target:
                return midpoint
            elif target < nums[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return -1


