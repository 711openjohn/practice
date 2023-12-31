#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.19%)
# Likes:    11793
# Dislikes: 221
# Total Accepted:    746.1K
# Total Submissions: 1.6M
# Testcase Example:  '[1,5,11,5]'
#
# Given an integer array nums, return true if you can partition the array into
# two subsets such that the sum of the elements in both subsets is equal or
# false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
#
#

from typing import List

# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i]:
                    continue
                dp[i] = i == num or dp[i - num]
        return dp[target]

        # total = sum(nums)
        # if total % 2 != 0:
        #     return False
        # target = total // 2
        # dp = [0] * (target + 1)
        # for i in range(len(nums)):
        #     for j in range(target, nums[i] - 1, -1):
        #         dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        # return dp[target] == target


# @lc code=end
Solution().canPartition([1, 5, 11, 5])
