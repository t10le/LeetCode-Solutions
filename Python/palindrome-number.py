class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is palindrome integer.

        An integer is a palindrome when it reads the same backward 
        as forward. For example, 121 is palindrome while 123 is not.
        """
        
        # mod 10 = gives you the last digit; work backwards
        # 121 <---
        # [1], [2], [1]
        
        if x < 0:
            return False
        
        x_copy = x
        i = 0
        while x > 1:
            # Extract last digit
            last_digit = x % 10
            
            # Truncate to iterate
            x = x // 10
            x = [121]
            
            # Cross reference
            x_copy mod 10**i
            i += 1

            
            
        121 // 10 = 12
        11 // 10 = 1
        10 // 10 = 1
        9 // 10 = 0
        
        121 mod 10**i
        121 mod 10**1 = 1
        121 mod 10**2 = 21
        121 mod 10**3 = 121
        
        
        > 121
        121 mod 10 = 1 <--
        121 // 10 = 12
        > 12
        12 mod 10 = 2 <--
        12 // 10 = 1
        > 1 
        1 mod 10 = 1 <--
        
        

        
        
        
        
        
        # -- Submission Stats (as of Oct 29, 2021) --
        # Time Complexity: O(n)
        # Runtime: 60ms, faster than 78.36%
        # Space Complexity: O(n)
        # Memory Usage: 14.1 MB, less than 77.60%
        
        # base case
#         if x < 0:
#             return False
        
        
#         #    [ -->0, 0, x, 0, 0<--]
#         s = str(x)
#         left = 0
#         right = len(s) - 1
#         while left <= right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
        
            
    
    
        # -- Submission Stats (as of Oct 29, 2021) --
        # Time Complexity: O(n)
        # Runtime: 56ms, faster than 86.92%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 49.91%
        
        # if x < 0:
        #     return False
        # return str(x) == str(x)[::-1]

        
        
        
        
