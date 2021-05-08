from typing import *


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        i = None # Row index
        j = None # Column index
        
        for row in range(len(board)):
            if "R" in board[row]:
                i = row             # Rook's row index
                j = board[row].index("R")  # Rook's column index
        
        output = 0 # Tracks the possible attacks
        
        def checkPawn(start, stop, step=1, direction=1):
            # Checking in the row (horizontally)
            if direction: 
                for k in range(start, stop, step):
                    if board[i][k] == "B":
                        return 0
                    elif board[i][k] == "p":
                        return 1
                    
            # Checking in the columns (vertically)
            else:        
                for k in range(start, stop, step):
                    if board[k][j] == "B":
                        return 0
                    elif board[k][j] == "p":
                        return 1
                    
            return 0
                
                
        ["p","p",".","R",".","p","B","."]
        # Case 1: Look to the left of the Rook
        output += checkPawn(j-1, -1, -1)

        # Case 2: Look to the right of the Rook
        output += checkPawn(j+1, len(board[i]))   
        
        # Case 3: Look above the Rook
        output += checkPawn(i-1, -1, -1, 0)
        
        # Case 4: Look below the Rook
        output += checkPawn(i+1, len(board), 1, 0)
        
        return output
