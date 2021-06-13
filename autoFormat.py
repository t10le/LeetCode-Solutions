# Make this script interact with readme.md
# -- Submission Stats (as of June 08, 2021) --
        # Time Complexity: O(n)
        # Runtime: 28ms, faster than 95.34%
        # Space Complexity: O(n)
        # Memory Usage: 14.3 MB, less than 49.29%

number = 617    
problemLink = "https://leetcode.com/problems/merge-two-binary-trees/"
problemTitle = problemLink[problemLink[:-
                                       1].rfind('/')+1:-1].replace('-', ' ').title()
solution = ""
time = "O(n)"
space = "O(1)"
difficulty = "Easy"
note = "if you're calling a built-in function more than once, use variables instead."

newTable = False

if not newTable:
    print('\n|{}| <a href="{}">{}</a> | <a href="{}">Python</a> |{}|{}|{}|{}|\n'.format(
        number, problemLink, problemTitle, solution, time, space, difficulty, note))
