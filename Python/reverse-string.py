class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Write a function that reverses a string. The input string is 
        given as an array of characters s.
        """
        
        # -- Submission Stats (as of Oct 26, 2021) --
        # Time Complexity: O(n)
        # Runtime: 196ms, faster than 85.45%
        # Space Complexity: O(1)
        # Memory Usage: 18.5 MB, less than 61.87%
        
        temp = ''
        left = 0
        right = len(s) - 1
        
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            left += 1
            right -= 1
        
        
        
        # -- Submission Stats (as of Oct 26, 2021) --
        # Time Complexity: O(n)
        # Runtime: 192ms, faster than 93.20%
        # Space Complexity: O(1)
        # Memory Usage: 18.5 MB, less than 83.17%
        
        # s.reverse()
        
        


