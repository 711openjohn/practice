# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock. 
# 
#  Return the maximum profit you can achieve from this transaction. If you 
# cannot achieve any profit, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you 
# must buy before you sell.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴
#  
#
#  Related Topics Array Dynamic Programming 👍 29463 👎 1029
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[-1][-1]

    # def maxProfit(self, prices: List[int]) -> int:
    #     dp = [[0] * 2 for _ in prices]
    #     dp[0][0] = -prices[0]
    #     for i in range(1, len(prices)):
    #         dp[i][0] = max(dp[i - 1][0], -prices[i])
    #         dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
    #     return dp[len(prices) - 1][1]

Solution().maxProfit([7,1,5,3,6,4])
