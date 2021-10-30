# LeetCode-Solutions
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<br>
Inspired by https://github.com/kamyu104/LeetCode-Solutions, I want to see if I can complete ALL 1723 LeetCode problems on my own. Let the journey begin!

## Array
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
| 999 | <a href="https://leetcode.com/problems/available-captures-for-rook/">Available Captures for Rook</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/available-captures-for-rook.py">Python</a> | O(n) | | Easy | Possible to do O(1)..Rework this |
|747| <a href="https://leetcode.com/problems/largest-number-at-least-twice-of-others/">Largest Number At Least Twice Of Others</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/largest-number-at-least-twice-of-others.py">Python</a> |O(n)|O(1)|Easy|Consider avoiding sort to improve time complexity, albeit it's still O(n) whether you sort or not.|
|1534| <a href="https://leetcode.com/problems/count-good-triplets/">Count Good Triplets</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/83cd23c0c3f2a54969695813a5af314a931c4213/Python/count-good-triplets.py">Python</a> |O(n^3)|O(n)|Easy|brute force...possible to do O(n^2) with Fenwick tree??|
|1572| <a href="https://leetcode.com/problems/matrix-diagonal-sum/">Matrix Diagonal Sum</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/matrix-diagonal-sum">Python</a> |O(n)|O(n)|Easy||

## String
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|7| <a href="https://leetcode.com/problems/reverse-integer/">Reverse Integer</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/reverse-integer.py">Python</a> |O(n)|O(n)|Easy||
| 67 | <a href="https://leetcode.com/problems/add-binary/">Add Binary</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/AddBinary.py">Python</a> | O(n) | | Easy | |
| 1108 | <a href="https://leetcode.com/problems/defanging-an-ip-address/submissions/">Defanging an IP Address</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/defang-an-ip-address.py">Python</a> | O(n) |  | Easy | |
|1544| <a href="https://leetcode.com/problems/make-the-string-great/">Make The String Great</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/make-the-string-great.py">Python</a> |O(n)|O(n)|Easy|it's possible to remove line 14; just don't index it weird; oddly, .pop(-1) performs better than .pop(), even though it does the same thing|
|1556| <a href="https://leetcode.com/problems/thousand-separator/">Thousand Separator</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/1556-thousand-separator.py">Python</a> |O(n)|O(n)|Easy|Cool math tricks|
| 1758 | <a href="https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/">Minimum Changes To Make Alternating Binary String</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/minimum-changes-to-make-alternating-binary-string.py"> Python</a>| O(n) | O(1) | Easy | |

## Bit Manipulation
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|268| <a href="https://leetcode.com/problems/missing-number/">Missing Number</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/missing-number.py">Python</a> |O(n)|O(1)|Easy|if you're calling a built-in function more than once, use variables instead.|
| 717 | <a href="https://leetcode.com/problems/1-bit-and-2-bit-characters/">1-bit and 2-bit Characters</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/OneBitTwoBitCharacters.py">Python</a> | O(n) |  | Easy | |


## Stack
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
| 456 | <a href="https://leetcode.com/problems/132-pattern/">132 Pattern</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/132Pattern.py">Python</a> | O(n) | | Medium | This was really hard to consider O(n) solution |


## Queue

## Binary Heap

## Tree
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|94| <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/">Binary Tree Inorder Traversal</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/binary-tree-inorder-traversal.py">Python</a> |O(n)|O(n)|Easy|iteration is more space efficient than recursion for inorder|
|144| <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/">Binary Tree Preorder Traversal</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/binary-tree-preorder-traversal.py">Python</a> |O(n)|O(n)|Easy|iteration with loop is faster than trival recursion.|
|145| <a href="https://leetcode.com/problems/binary-tree-postorder-traversal/">Binary Tree Postorder Traversal</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/binary-tree-postorder-traversal.py">Python</a> |O(n)|O(n)|Easy|iteration is faster than recursion|
|617| <a href="https://leetcode.com/problems/merge-two-binary-trees/">Merge Two Binary Trees</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/merge-two-binary-trees.py">Python</a> |O(n)|O(n)|Easy||

## Hash Table
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
| 1 | <a href="https://leetcode.com/problems/two-sum/">Two Sum</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/TwoSum.py">Python</a> |  | | Easy | Slow AF, highly inefficient...rework using hash table |
|748| <a href="https://leetcode.com/problems/shortest-completing-word/">Shortest Completing Word</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/shortest-completing-word.py">Python</a> |O(n^2)|O(n)|Easy|not space efficient, must rework using hash table.|


## Math
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|9| <a href="https://leetcode.com/problems/palindrome-number/">Palindrome Number</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/palindrome-number.py">Python</a> |O(n)|O(n)|Easy|Use of mod 10 and floor div 10 to iterate an integer without type cast|
| 258 | <a href="https://leetcode.com/problems/add-digits/">Add Digits</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/add-digits.py">Python</a> | O(1) | O(1) | Easy | Recursion/loop is trival; to get O(1), you must use digital root properties instead|

## Sort

## Two Pointers
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|344| <a href="https://leetcode.com/problems/reverse-string/">Reverse String</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/reverse-string.py">Python</a> |O(n)|O(1)|Easy||
|557| <a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/">Reverse Words In A String Iii</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/reverse-words-in-a-string-3.py">Python</a> |O(n)|O(n)|Easy||
|977| <a href="https://leetcode.com/problems/squares-of-a-sorted-array/">Squares Of A Sorted Array</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/squares-of-a-sorted-array.py">Python</a> |O(n)|O(1)|Easy|use of raw pointers on a dummy list

## Recursion

## Binary Search
| # | Title | Solution | Time | Space | Difficulty | Personal Note
|---| ---| ---| ---| ---| ---| ---|
|7| <a href="https://leetcode.com/problems/binary-search/">Binary Search</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/binary-search.py">Python</a> |O(log(n))|O(1)|Easy||
|35| <a href="https://leetcode.com/problems/search-insert-position/">Search Insert Position</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/search-insert-position.py">Python</a> |O(log(n))|O(1)|Easy||
|278| <a href="https://leetcode.com/problems/first-bad-version/">First Bad Version</a> | <a href="https://github.com/t10le/LeetCode-Solutions/blob/main/Python/first-bad-version.py">Python</a> |O(log(n))|O(1)|Easy|slightly modified binary search|

## Binary Search Tree

## Breadth-First Search

## Depth-First Search

## Backtracking

## Dynamic Programming

## Greedy

## Graph

## Geometry

## Simulation

## Design

## Concurrency

## SQL

## Shell Script
