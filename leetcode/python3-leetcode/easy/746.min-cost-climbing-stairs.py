#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (65.16%)
# Likes:    10990
# Dislikes: 1664
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '[10,15,20]'
#
# You are given an integer array cost where cost[i] is the cost of i^th step on
# a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
# Example 1:
#
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#
#
# Example 2:
#
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
#
# Constraints:
#
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
#
#
#
from typing import List


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return 0

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # [10,15,20] -> 15
    #     # [0,0,0]
    #     n = len(cost)
    #     dp = [0] * (n + 1)
    #     for i in range(2, n + 1):
    #         dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    #     return dp[n]

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     n = len(cost)
    #     dp = [0] * (n + 1)

    #     # [1,100,1,1,1,100,1,1,100,1]
    #     for i in range(2, n + 1):
    #         cost_i = i - 1
    #         dp[i] = min(dp[i - 1] + cost[cost_i], dp[i - 2] + cost[cost_i - 1])

    #     return dp[n]


# @lc code=end
Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
