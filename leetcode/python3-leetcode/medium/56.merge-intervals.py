#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (46.74%)
# Likes:    21313
# Dislikes: 729
# Total Accepted:    2.2M
# Total Submissions: 4.6M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#
from typing import List

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     if len(intervals) == 1:
    #         return intervals
    #     intervals.sort(key=lambda x: x[0])
    #     result = [intervals[0]]
    #     for i in range(1, len(intervals)):
    #         previous = result[-1]
    #         current = intervals[i]
    #         if current[0] <= previous[1]:
    #             previous[1] = max(current[1], previous[1])
    #         else:
    #             result.append(current)
    #     return result


# @lc code=end

Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
