from typing import *


class Solution:
    def minOperations(self, s: str) -> int:
        return min(s[::2].count("1") + s[1::2].count("0"), s[::2].count("0") + s[1::2].count("1"))
