class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given a string s, reverse the order of characters in each word within 
        a sentence while still preserving whitespace and initial word order.
        """

        # -- Submission Stats (as of Oct 27, 2021) --
        # Time Complexity: O(n)
        # Runtime: 80ms, faster than 25.88%
        # Space Complexity: O(n)
        # Memory Usage: 15.1 MB, less than 28.78%
        
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]

    
        # -- Submission Stats (as of Oct 27, 2021) --
        # Time Complexity: O(n)
        # Runtime: 28ms, faster than 95.87%
        # Space Complexity: O(n)
        # Memory Usage: 14.8 MB, less than 62.17%
        
        # return ' '.join(s.split()[::-1])[::-1]
        
        
        # -- Submission Stats (as of Oct 27, 2021) --
        # Time Complexity: O(n)
        # Runtime: 28ms, faster than 95.87%
        # Space Complexity: O(n)
        # Memory Usage: 15.0 MB, less than 28.78%

        # i = s[::-1].split()
        # ii = [a[x] for x in range(len(a)-1, -1, -1)]
        # return ' '.join(ii)
        
        
        # -- Submission Stats (as of Oct 27, 2021) --
        # Time Complexity: O(n)
        # Runtime: 36ms, faster than 76.69%
        # Space Complexity: O(n)
        # Memory Usage: 14.8 MB, less than 75.25%
        
        # i = s[::-1].split()
        # i.reverse()
        # return ' '.join(i)
        
        



