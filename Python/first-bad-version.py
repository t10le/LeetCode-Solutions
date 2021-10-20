# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # SOLUTION
        # -- Submission Stats (as of Oct 19, 2021) --
        # Time Complexity: O(log(n))
        # Runtime: 28ms, faster than 84.47%
        # Space Complexity: O(1)
        # Memory Usage: 14.2 MB, less than 72.75%
        
        # base case
        if n == 1: 
            return 1
        
        left = 1
        right = n
        while left <= right:
            mid = left + ((right-left) // 2)
            # print(f"mid: {mid}")
            
            # if mid is bad(true), then either you are directly on the latest bad version,
            # or you have to search further to the left for the latest.
            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    right = mid - 1
                    # print(f"right: {right}")
                else:
                    return mid
                    # print(f"mid: {mid}")
            
            # if mid is not bad, then it must be on the right side.
            # re-evaluate the new block by discarding the left side.
            else:
                left = mid + 1
                # print(f"left:{left}")
                 
                
