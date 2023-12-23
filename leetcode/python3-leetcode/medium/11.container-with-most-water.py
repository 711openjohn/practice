#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.36%)
# Likes:    27420
# Dislikes: 1532
# Total Accepted:    2.5M
# Total Submissions: 4.6M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#


# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_a = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_a = max(max_a, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_a

    # def maxArea(self, height: List[int]) -> int:
    #     l = 0
    #     r = len(height) - 1
    #     max_area = (r - l) * (min(height[l], height[r]))
    #     while l < r:
    #         area = (r - l) * (min(height[l], height[r]))
    #         if height[l] > height[r]:
    #             r -= 1
    #         else:
    #             l += 1
    #         max_area = max(max_area, area)
    #     return max_area


# @lc code=end
Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
