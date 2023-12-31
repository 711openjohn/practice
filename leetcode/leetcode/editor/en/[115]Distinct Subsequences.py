# Given two strings s and t, return the number of distinct subsequences of s 
# which equals t. 
# 
#  The test cases are generated so that the answer fits on a 32-bit signed 
# integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
#  
# 
#  Example 2: 
# 
#  
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 1000 
#  s and t consist of English letters. 
#  
# 
#  👍 6367 👎 279


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return 0

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(len(t)):
            dp[0][j] = 0
        dp[0][0] = 1
        #dp[i][j]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
