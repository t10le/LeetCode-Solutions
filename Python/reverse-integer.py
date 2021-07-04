from typing import *


class Solution:
    def reverse(self, x: int) -> int:
        """Given a signed 32-bit integer x, return x with its digits reversed."""

        # -- Submission Stats (as of July 03, 2021) --
        # Time Complexity: O(n)
        # Runtime: 36ms, faster than 41.7%
        # Space Complexity: O(n)
        # Memory Usage: 14.1 MB, less than 90.14%

        s = (x > 0) - (x < 0)
        r = int(str(s*x)[::-1])
        if r < 2**31-1 and r > -2**31:
            return r*s
        return 0


"""
-- notes --
12010 / 10000 = 1.201 * 1000 = 1201.0 = 1201

(1201000000000000 / 1000000000000000) = 1.201 * 1000 = 1201.0 = 1201

-1230 = -321

int("0321") -> 321 ; int removes leading zeros.
"""
