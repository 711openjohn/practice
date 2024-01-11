# Given an m x n matrix board containing 'X' and 'O', capture all regions that 
# are 4-directionally surrounded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded 
# region. 
# 
#  
#  Example 1: 
#  
#  
# Input: board = [
# ["X","X","X","X"],
# ["X","O","O","X"],
# ["X","X","O","X"],
# ["X","O","X","X"]]
# Output: [
# ["X","X","X","X"],
# ["X","X","X","X"],
# ["X","X","X","X"],
# ["X","O","X","X"]
# ]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["X"]]
# Output: [["X"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] is 'X' or 'O'. 
#  
# 
#  👍 8244 👎 1716
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()

        def is_border(i, j, board):
            if (i, j) in seen:
                return False
            if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                return True
            return False

        def mark(i, j):
            board[i][j] = '@'
            seen.add((i, j))
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for move in moves:
                new_x = i + move[0]
                new_y = j + move[1]
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and (new_x, new_y) not in seen and board[new_x][new_y] == 'O':
                    mark(new_x, new_y)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_border(i, j, board):
                    mark(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '@':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'



# leetcode submit region end(Prohibit modification and deletion)

Solution().solve([
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"]])
