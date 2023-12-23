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

        def is_board(x, y):
            return x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1

        def is_valid(x, y):
            if (x, y) in seen:
                return False
            if x < 0:
                return False
            if y < 0:
                return False
            if x >= len(board):
                return False
            if y >= len(board[0]):
                return False

            if board[x][y] == 'O':
                return True

            return False

        def dfs(i, j):
            board[i][j] = "y"
            seen.add((i, j))
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                x, y = i + dx, j + dy
                if is_valid(x, y):
                    dfs(x, y)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and is_board(i, j):
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "y":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board

    # def solve(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: None Do not return anything, modify board in-place instead.
    #     """
    #     n, m = len(board), len(board[0])
    #     seen = set()

    #     def is_valid(i, j):
    #         return (
    #             0 <= i < n and 0 <= j < m and board[i][j] == "O" and (i, j) not in seen
    #         )

    #     def is_border(i, j):
    #         return i == 0 or i == n - 1 or j == 0 or j == m - 1

    #     def dfs(i, j):
    #         board[i][j] = "y"
    #         seen.add((i, j))
    #         for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    #             new_i, new_j = dx + i, dy + j
    #             if is_valid(new_i, new_j):
    #                 dfs(new_i, new_j)

    #     for i in range(n):
    #         for j in range(m):
    #             if is_border(i, j) and board[i][j] == "O":
    #                 dfs(i, j)

    #     for i in range(n):
    #         for j in range(m):
    #             if board[i][j] == "y":
    #                 board[i][j] = "O"
    #             else:
    #                 board[i][j] = "X"
    #     return board


# @lc code=end

Solution().solve(
    [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "X", "X"],
    ]
)
