#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.42%)
# Likes:    8185
# Dislikes: 1704
# Total Accepted:    629.2K
# Total Submissions: 1.6M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#


# @lc code=start
class Solution(object):
    def solve(self, board):
        seen = set()

        def is_valid(x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            if (x, y) in seen:
                return False
            if board[x][y] != "O":
                return False
            return True

        def dfs(x, y):
            print(x, y)
            board[x][y] = "y"
            seen.add((x, y))
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in moves:
                nx = x + dx
                ny = y + dy
                if is_valid(nx, ny):
                    dfs(nx, ny)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board) - 1) and board[i][j] == "O":
                    dfs(i, j)
                elif (j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "y":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return board


# @lc code=end

Solution().solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
