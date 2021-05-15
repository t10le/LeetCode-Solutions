from typing import *


class Solution:
    def makeGood(self, s: str) -> str:
        # Remove all pairs of adjacent upperLowers
        pair = lambda x, y: x != y

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

        if len(s) == 1:
            return s

        result = ""
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:

