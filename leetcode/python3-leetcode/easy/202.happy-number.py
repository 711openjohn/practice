#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (55.54%)
# Likes:    9827
# Dislikes: 1318
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            happy = 0
            for c in str(n):
                happy += int(c) ** 2
            if happy == 1:
                return True
            n = happy
        return False

    # def isHappy(self, n: int) -> bool:
    #     record = set()
    #     while n not in record:
    #         record.add(n)
    #         new_num = 0
    #         for s in str(n):
    #             new_num += int(s) ** 2
    #         if new_num == 1:
    #             return True
    #         n = new_num
    #     return False


# @lc code=end
Solution().isHappy(2)
