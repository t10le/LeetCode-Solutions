from typing import *


class Solution:
    def makeGood(self, s: str) -> str:
        """Returns the 'good' copy of the given string, 's', which is a string that does not have two adjacent characters that are equal in alphabetical value and the pair contains an upper and lower-case character."""
        # -- Even --
        # aABb --> ""
        # abBA --> ""
        # aAbc --> "bc"
        # abAc --> "abAc"

        # -- Odd --
        # aAb --> 'b'
        # a --> 'a'
        # aBaAbc --> 'ac'
        # aBc --> 'aBc'

        # -- Submission Stats (as of May 16, 2021) --
        # Time Complexity: O(n)
        # Runtime: 28ms, faster than 95.34%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 49.29%

        if len(s) == 1:
            return s

        # treat result like a stack
        result = [s[0]]

        for i in range(1, len(s)):
            # if the 'result' list is not empty, compare elements and indices
            if result:
                if result[-1].lower() == s[i].lower() and result[-1] != s[i]:
                    result.pop(-1)
                else:
                    result.append(s[i])
            else:
                result.append(s[i])

        return "".join(e for e in result)
