from typing import *


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_nums[i]:
                while stack != [] and stack[-1] <= min_nums[i]:
                    stack.pop()
                stack.append(nums[i])
                # print(stack)
                if len(stack) >= 2 and stack[-1] > stack[-2]:
                    return True
                # print(stack)

        # print(min_nums)
        # print(stack)
        return False


a = Solution()
# a.find132pattern([-1, 3, 2, 0])
# a.find132pattern([-1, 0, 1, 2])
a.find132pattern([1, 0, 1, -4, -3])
# print(a.find132pattern([1, 2, 3, 4]))
# print(a.find132pattern([3, 1, 4, 2]))
# print(a.find132pattern([-1, 3, 2, 0]))
# a.find132pattern([2, 4, 3, 0])
a.find132pattern([5, 3, 2, 4, 3, -1])
# a.find132pattern([2, -1, 5, 4, 0])


print(a.find132pattern([1, 0, 1, -4, -3]))
print(a.find132pattern([5, 3, 2, 4, 3, -1]))
'''
The [0] number must be the smallest number, where [1] must be the greatest.
If [1] is less than or equal to [0], or [2] is greater than or equal to [1], it fails.

Notes
- In both odd and even degree arrays, the highest number cannot be in head or tail of the list.
- If the array is sorted in either an ascending or descending order, it is an automatic fail.
- The number of opportunities for a 132 pattern is `len(num) - 2`, since the pattern cannot
  exist at either the head or tail of list.

STRATEGY
1) Form an array with all lowest values relative to each index by detaching the head of the list with each iteration.
   The reason is that the lowest value must be on the furthest left side, and by keeping it relative to the position,
   if the value is lower than the previous values, that is an opportunity for a new 132 sequence,which must be 
   accounted for.
2) Now start in reverse order, since the goal is to find values greater than the lowest value relative to their position
   formed from the array in step one; in other words, the goal is find either the sequence 132 or 123. Clearly, 132 is
   ideal, but that is where step three comes to filter.
3) Upon each iteration of the reverse order, check if the stack is lower or equal to the lowest value relative to the 
   current iteration. The reason is that the topmost of the stack should represent '3' in the sequence, where it is greater
   than the lowest value, and the value below its stack. If not, keep removing the topmost stack.

For example,
arr = [5, 3, 2, 4, 3, -1]
min = [5, 3, 2, 2, 2, -1] <- lowest values relative to each index

Starting in reverse order:
> is -1 greater than -1? No. Do not add to stack.
> is 3 greater than 2? Yes, this is a potential 132 or 123 sequence, where you can see that 2 is on the left, and 3 is higher
  then 2 and is on the right. Now we just need the middle value. Add to stack.
> is 4 greater than 2? Yes, this is potentially the middle value for 132 or 123. Hopefully it's 132. Now is a good time to check!
  Is 4 greater than 3, which means it's also greater than 2? Yes. Thus, since 2 is on the furthest left (determined by our array
  in step one) and 3 is on the furtherest right (determined by checking if the value is greater than the lowest value relative
  to its position).
> True
'''
