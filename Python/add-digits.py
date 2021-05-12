from typing import *


class Solution:
    def addDigits(self, num: int) -> int:
        """
        This equation is supposed to calculate the digital root of a number

        There are properties of a digital root, in summary:
        - If we multiply any number by 9, the digital root will always be 9.
        - Adding 9 to a number does not change the digital root of that number.
        - If we divide any number by 9, the digital root of that number will be the remainder.

        Use the last property to obtain O(1) time complexity solution.
        """

        # By the first propety of a digital root, any multiples of 9s will always have
        # a digit root equal to 9.
        # Special case is considered when the number is 0, where 0 mod 9 is not 9, it's 0.
        # By the third property of a digital root, the digital root of any number will be
        # the remainder of that number divided by 9.
        return num % 9 if (num % 9 != 0 or num == 0) else 9
