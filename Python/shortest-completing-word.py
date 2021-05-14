from typing import *


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # finding intersection would work beautifully if substring was unique

        # edge case: if collision, use the first shortest occurrence

        # Filter out the numbers in licensePlate.
        # Substring must be lowercase for proper comparison.
        # If word contains all letters.
        # If word is the shortest.
        # By design of loop, first shortest occurrence that contains all letters
        # will be picked.
        def compare(x, y):
            for e in y:
                if e not in x:
                    return False
                x.remove(e)
            return True

        onlyChars = list(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([e for e in words if compare(list(e), onlyChars)], key=len)



        # [e.lower() for e in licensePlate if e.isalpha()]
        # "".join(filter(lambda x: x.isalpha(), licensePlate))
        # [e for e in words if e in onlyChars]
