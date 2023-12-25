#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (57.16%)
# Likes:    4823
# Dislikes: 138
# Total Accepted:    313.1K
# Total Submissions: 547.8K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
#
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
#
# Example 1:
#
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
#
#
# Example 2:
#
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
#
# Constraints:
#
#
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
#
#
#
from typing import List

# @lc code=start


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        prev_group = {}
        for n1 in nums1:
            for n2 in nums2:
                prev_group[n1 + n2] = prev_group.get(n1 + n2, 0) + 1
        result = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -1 * (n3 + n4)
                result += prev_group.get(key, 0)
        return result


# @lc code=end
Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
