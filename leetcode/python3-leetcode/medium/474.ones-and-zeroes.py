#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (47.26%)
# Likes:    5285
# Dislikes: 438
# Total Accepted:    191.1K
# Total Submissions: 404.1K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# You are given an array of binary strings strs and two integers m and n.
#
# Return the size of the largest subset of strs such that there are at most m
# 0's and n 1's in the subset.
#
# A set x is a subset of a set y if all elements of x are also elements of
# y.
#
#
# Example 1:
#
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10",
# "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the
# maximum of 3.
#
#
# Example 2:
#
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
#
#
#
from typing import List

# @lc code=start


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        for s in strs:
            ones = 0
            zeros = 0
            for c in s:
                if c == "0":
                    zeros += 1
                else:
                    ones += 1
            cache[s] = [zeros, ones]

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            [zeros, ones] = cache[s]
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]

    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     cache = {}
    #     for s in strs:
    #         zeros = 0
    #         ones = 0
    #         for c in s:
    #             if c == "0":
    #                 zeros += 1
    #             else:
    #                 ones += 1
    #         cache[s] = [zeros, ones]

    #     # dp[m][n]
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]
    #     for s in strs:
    #         zeros = cache[s][0]
    #         ones = cache[s][1]
    #         for i in range(m, zeros - 1, -1):
    #             for j in range(n, ones - 1, -1):
    #                 dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    #     return dp[m][n]

    # dp = [[0] * (n + 1) for _ in range(m + 1)]  # 创建二维动态规划数组，初始化为0
    # for s in strs:  # 遍历物品
    #     zeroNum = s.count('0')  # 统计0的个数
    #     oneNum = len(s) - zeroNum  # 统计1的个数
    #     for i in range(m, zeroNum - 1, -1):  # 遍历背包容量且从后向前遍历
    #         for j in range(n, oneNum - 1, -1):
    #             dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)  # 状态转移方程
    # return dp[m][n]


# @lc code=end
Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
