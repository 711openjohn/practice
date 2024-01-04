# Write an algorithm to determine if a number n is happy. 
# 
#  A happy number is a number defined by the following process: 
# 
#  
#  Starting with any positive integer, replace the number by the sum of the 
# squares of its digits. 
#  Repeat the process until the number equals 1 (where it will stay), or it 
# loops endlessly in a cycle which does not include 1. 
#  Those numbers for which this process ends in 1 are happy. 
#  
# 
#  Return true if n is a happy number, and false if not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 19
# Output: true
# Explanation:
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  👍 9858 👎 1332


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        exists = set()
        while n not in exists:
            result = 0
            exists.add(n)
            for c in str(n):
                result += int(c) * int(c)
            if result == 1:
                return True
            n = result
        return False

# leetcode submit region end(Prohibit modification and deletion)
