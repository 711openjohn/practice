#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (33.65%)
# Likes:    29390
# Dislikes: 2670
# Total Accepted:    3.2M
# Total Submissions: 9.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                local_sum = nums[i] + nums[l] + nums[r]
                if local_sum < 0:
                    l += 1
                elif local_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    r -= 1
                    l += 1
        return result

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     nums.sort()

    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             return result

    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue

    #         left = i + 1
    #         right = len(nums) - 1

    #         while right > left:
    #             sum_ = nums[i] + nums[left] + nums[right]

    #             if sum_ < 0:
    #                 left += 1
    #             elif sum_ > 0:
    #                 right -= 1
    #             else:
    #                 result.append([nums[i], nums[left], nums[right]])
    #                 while right > left and nums[right] == nums[right - 1]:
    #                     right -= 1
    #                 while right > left and nums[left] == nums[left + 1]:
    #                     left += 1

    #                 right -= 1
    #                 left += 1

    #     return result


# @lc code=end
