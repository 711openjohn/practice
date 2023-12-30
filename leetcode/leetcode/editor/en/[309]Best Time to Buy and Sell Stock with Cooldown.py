# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  Find the maximum profit you can achieve. You may complete as many 
# transactions as you like (i.e., buy one and sell one share of the stock multiple times) 
# with the following restrictions: 
# 
#  
#  After you sell your stock, you cannot buy stock on the next day (i.e., 
# cooldown one day). 
#  
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 5000 
#  0 <= prices[i] <= 1000 
#  
# 
#  👍 9101 👎 304
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 4 for _ in range(n)]
        # 创建动态规划数组，4个状态分别表示
        # 持有股票、
        # 不持有股票且处于冷冻期、
        # 不持有股票且不处于冷冻期、
        # 不持有股票且当天卖出后处于冷冻期
        dp[0][0] = -prices[0]  # 初始状态：第一天持有股票的最大利润为买入股票的价格
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[
                i])  # 当前持有股票的最大利润等于前一天持有股票的最大利润或者前一天不持有股票且不处于冷冻期的最大利润减去当前股票的价格
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])  # 当前不持有股票且处于冷冻期的最大利润等于前一天持有股票的最大利润加上当前股票的价格
            dp[i][2] = dp[i - 1][0] + prices[i]  # 当前不持有股票且不处于冷冻期的最大利润等于前一天不持有股票的最大利润或者前一天处于冷冻期的最大利润
            dp[i][3] = dp[i - 1][2]  # 当前不持有股票且当天卖出后处于冷冻期的最大利润等于前一天不持有股票且不处于冷冻期的最大利润
        return max(dp[n - 1][3], dp[n - 1][1], dp[n - 1][2])  # 返回最后一天不持有股票的最大利润
# leetcode submit region end(Prohibit modification and deletion)
