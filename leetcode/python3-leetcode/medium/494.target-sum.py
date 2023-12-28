#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.26%)
# Likes:    10443
# Dislikes: 340
# Total Accepted:    538.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+'
# and '-' before each integer in nums and then concatenate all the
# integers.
#
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
#
#
# Return the number of different expressions that you can build, which
# evaluates to target.
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be
# target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
# Example 2:
#
#
# Input: nums = [1], target = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0:
            return 0
        if abs(target) > total:
            return 0

        left = (target + total) // 2
        dp = [0] * (left + 1)
        dp[0] = 1
        for num in nums:
            for i in range(left, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[left]


# @lc code=end
