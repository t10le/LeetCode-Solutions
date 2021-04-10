from typing import *


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.split(".")  # this is an array

        result = ""

        # space complex --> 4 --> caps out at some point...
        # time  --> o(n)
        # space --> o(n)

        for val in defanged:
            result += val
            result += "[.]"

        return result[0:len(result)-3]
        # --- alternatives ---
        # return "[.]".join(address.split("."))
