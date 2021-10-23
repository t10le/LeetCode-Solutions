class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return an array of the squares 
        of each number sorted in non-decreasing order.
        
        auxiliary space = extra space or temporary space used by an algorithm.
        space complexity = total space taken by the algorithm relative to input size.
        """
        # -- Submission Stats (as of Oct 23, 2021) --
        # Time Complexity: O(n)
        # Runtime: 224 ms, faster than 79.81%
        # Space Complexity: O(1)
        # Memory Usage: 16.1 MB, less than 74.57%
        
        # Initialize dummy array with writer pointer
        answer = [0] * len(nums)
        writer = len(answer) - 1
        
        # Initialize left and right pointers
        left = 0
        right = len(answer) - 1
        
        # strat: Start at the end of the 'sorted' answer list and search for values
        #        that will be higher than the other, based on pointer values.
        while writer >= 0:
            lsq = nums[left]**2
            rsq = nums[right]**2
            
            # Compete for the highest value spot towards the right [..,x]
            if lsq > rsq:
                # Left-square wins, so left-square secures the 'x' spot
                answer[writer] = lsq
                left += 1
            else:
                # Right-square wins, or equal, so arbitrary right-square secures 'x' spot
                answer[writer] = rsq
                right -= 1
                
            writer -= 1
            
        return answer
                
        
        
        # -- Submission Stats (as of Oct 23, 2021) --
        # Time Complexity: O(n)
        # Runtime: 200 ms, faster than 98.41%
        # Space Complexity: O(1)
        # Memory Usage: 15.8 MB, less than 94.42%
        
        # strat: overwrite contents, but ask interviewer if this is ok
       
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        # nums.sort()
        # return nums
        
        
        
        
        # -- Submission Stats (as of Oct 23, 2021) --
        # Time Complexity: O(n)
        # Runtime: 228 ms, faster than 99.86%
        # Space Complexity: O(n)
        # Memory Usage: 16.3 MB, less than 42.29%
        
        # strat: declaring another block of memory for new sorted
        
        # a = [x**2 for x in nums]
        # a.sort()
        # return a

    
    
    
        # -- Submission Stats (as of Oct 23, 2021) --
        # Time Complexity: O(n)
        # Runtime: 224 ms, faster than 79.81%
        # Space Complexity: O(n)
        # Memory Usage: 16.1 MB, less than 74.57%
        
        # strat: one-liner, but list comprehension must be garbage collected when returned
        # memory was momentarily stored prior to the garbage collect (auxillary space)
        
        # return sorted([x**2 for x in nums])
        
        
        
