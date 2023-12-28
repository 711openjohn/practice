#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (43.21%)
# Likes:    18157
# Dislikes: 423
# Total Accepted:    1.6M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#
from typing import List

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


# @lc code=end

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for coin in coins:
#             for i in range(coin, amount + 1): # 进行优化，从能装得下的背包开始计算，则不需要进行比较
#                 # 更新凑成金额 i 所需的最少硬币数量
#                 dp[i] = min(dp[i], dp[i - coin] + 1)

#         return dp[amount] if dp[amount] != float('inf') else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for i in range(1, amount + 1):  # 遍历背包容量
#             for coin in coins:  # 遍历物品
#                 if i - coin >= 0:
#                     # 更新凑成金额 i 所需的最少硬币数量
#                     dp[i] = min(dp[i], dp[i - coin] + 1)

#         return dp[amount] if dp[amount] != float('inf') else -1
