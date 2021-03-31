from typing import *


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Returns the sum of two binary strings as a binary string.
        `a` and `b` consist only of `0` or `1` characters.
        Each string does not contain leading zeros except for only zero itself.
            E.g. 0001 -> bad
                 01 -> bad
                 0 -> good
                 1 -> good
                 10 -> good
                 100 -> good
                 101 -> good
        """
        c = str(int(a) + int(b))
        result = ""
        flag = False
        for i in range(len(c) - 1, -1, -1):
            if not flag:
                if c[i] == "2":
                    flag = True
                    result = "0" + result
                elif c[i] == "1":
                    result = "1" + result
                else:
                    result = "0" + result
            else:
                if c[i] == "2":
                    result = "1" + result
                elif c[i] == "1":
                    result = "0" + result
                else:
                    flag = False
                    result = "1" + result
        if flag:
            result = "1" + result
        return result
