#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (60.02%)
# Likes:    4968
# Dislikes: 430
# Total Accepted:    339.4K
# Total Submissions: 565.2K
# Testcase Example:  '2'
#
# Given an integer n, break it into the sum of k positive integers, where k >=
# 2, and maximize the product of those integers.
#
# Return the maximum product you can get.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#
# Example 2:
#
#
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#
#
# Constraints:
#
#
# 2 <= n <= 58
#
#
#


# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * (i - j), dp[(i - j)] * j)
        return dp[n]


# @lc code=end
Solution().integerBreak(8)
