#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (51.18%)
# Likes:    53456
# Dislikes: 1771
# Total Accepted:    11.5M
# Total Submissions: 22.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#
from typing import List

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) not in cache:
                cache[n] = i
                continue

            return [cache[target - n], i]
        return []

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     cache = {}
    #     for idx, num in enumerate(nums):
    #         side = target - num
    #         if side in cache:
    #             return [cache.get(side), idx]
    #         else:
    #             cache[num] = idx
    #     return []


# @lc code=end
print(Solution().twoSum([2, 7, 11, 15], 9))
