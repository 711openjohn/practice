#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (70.38%)
# Likes:    6152
# Dislikes: 249
# Total Accepted:    537.6K
# Total Submissions: 763K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#
from typing import List

# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 0

        def is_valid(x, y):
            if x < 0 or y < 0 or y >= n or x >= n:
                return False
            if result[x][y] != 0:
                return False
            return True

        sx = 0
        sy = 0
        move = moves[0]
        for i in range(n * n):
            v = i + 1
            result[sx][sy] = v
            nx = sx + move[0]
            ny = sy + move[1]
            if not is_valid(nx, ny):
                curr = (curr + 1) % 4
                move = moves[curr]
                nx = sx + move[0]
                ny = sy + move[1]
            sx = nx
            sy = ny
        return result


# @lc code=end
Solution().generateMatrix(4)
