#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (53.07%)
# Likes:    10258
# Dislikes: 426
# Total Accepted:    717.2K
# Total Submissions: 1.4M
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
#
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    # def numSquares(self, n: int) -> int:
    #     dp = [float("inf")] * (n + 1)
    #     dp[0] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, int(i**0.5) + 1):
    #             dp[i] = min(dp[i], dp[i - j * j] + 1)
    #     return dp[n]


# @lc code=end

Solution().numSquares(12)
# dp = [float('inf')] * (n + 1)
# dp[0] = 0

# for i in range(1, n + 1):  # 遍历背包
#     for j in range(1, int(i ** 0.5) + 1):  # 遍历物品
#         # 更新凑成数字 i 所需的最少完全平方数数量
#         dp[i] = min(dp[i], dp[i - j * j] + 1)

# return dp[n]
