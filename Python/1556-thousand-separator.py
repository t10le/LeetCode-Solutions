from typing import *


class Solution:
    def thousandSeparator(self, n: int) -> str:
        """Returns the string format of an integer with thousands separator as a dot."""
        # -- Submission Stats (as of May 21, 2021) --
        # Time Complexity: O(n)
        # Runtime: 16ms, faster than 99.86%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 42.29%
        s = str(n)
        x = len(s)

        if x < 4:
            return s

        result = str(int(n/10**(x - ((x - 1) % 3 + 1))))
        li = list(s)

        i = len(str(int(n/10**(x - ((x - 1) % 3 + 1)))))
        while i < x:
            li.insert(i, '.')
            i += 4

        return "".join(li)
