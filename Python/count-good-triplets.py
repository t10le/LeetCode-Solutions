from typing import *


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """Returns the integer of how many good triplets exist in a given array of integers"""
        # -- Submission Stats (as of May 19, 2021) --
        # Time Complexity: O(n^3)
        # Runtime: 372ms, faster than 86.15%
        # Space Complexity: O(n)
        # Memory Usage: 14.2 MB, less than 83.59%
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        # cond1 = 0 <= i < j < k < len(arr)
                        # removed cond1 because len-2 and len-1 covers this condition
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1

        return count


        # (i, j, k)
        # i-j <= a
        # j-k <= b
        # i-k <= c
        # i < j < k < arr.length

        # Sort the arr
        # [0,1,1,3,7,9]

        # evaluate i-j <= a
