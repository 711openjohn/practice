# You are given an integer array prices where prices[i] is the price of a given 
# stock on the iᵗʰ day, and an integer k. 
# 
#  Find the maximum profit you can achieve. You may complete at most k 
# transactions: i.e. you may buy at most k times and sell at most k times. 
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 
# 4-2 = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3
# -0 = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 100 
#  1 <= prices.length <= 1000 
#  0 <= prices[i] <= 1000 
#  
# 
#  👍 7185 👎 204
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        # trades = len(prices) // 2 * 2
        trades = k * 2
        dp = [[0] * (trades + 1) for _ in prices]
        for j in range(1, trades + 1):
            if j % 2 == 1:
                dp[0][j] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            for j in range(1, trades + 1):
                if j % 2 != 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j-1] + prices[i])

        return dp[-1][trades]

# leetcode submit region end(Prohibit modification and deletion)

Solution().maxProfit(2, [3,2,6,5,0,3])