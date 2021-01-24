class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Returns the indices of two numbers that add up to 'target' '''
        i = 0
        found = False

        while i != len(nums) and not found:
            ans = target - nums[i]
            if ans in nums:
                j = i
                try:
                    k = nums.index(ans, i+1, len(nums))
                    found = True
                except ValueError:
                    pass
            i += 1

        return [j, k]
