class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the       target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
        """
        
        # SOLUTION
        # -- Submission Stats (as of Oct 20, 2021) --
        # Time Complexity: O(log(n))
        # Runtime: 48ms, faster than 81.03%
        # Space Complexity: O(1)
        # Memory Usage: 15.2 MB, less than 23.29%
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        
        if nums[mid] < target:
            return mid + 1
        return mid
