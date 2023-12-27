#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (43.54%)
# Likes:    4518
# Dislikes: 466
# Total Accepted:    422.8K
# Total Submissions: 970.9K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity?
# How and why?
#
#
#
#

from typing import List

# @lc code=start

# 123 4 567

# 712 3 456
# 671 2 345
# 567 1 234

# 456 7 123
# 345 6 712
# 234 5 671


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m if nums[m] != nums[r] else r - 1
        return nums[l]

    # def findMin(self, nums: List[int]) -> int:
    #     l = 0
    #     r = len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] > nums[r]:
    #             l = mid + 1
    #         else:
    #             r = mid if nums[r] != nums[mid] else r - 1
    #     return nums[l]

    # def findMin(self, nums: List[int]) -> int:
    #     l = 0
    #     r = len(nums) - 1

    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] > nums[r]:
    #             l = mid + 1
    #         else:
    #             r = mid if nums[r] != nums[mid] else r - 1
    #     return nums[l]


# @lc code=end
Solution().findMin([5, 6, 7, 1, 2, 3, 4])
