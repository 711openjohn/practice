#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (41.05%)
# Likes:    5204
# Dislikes: 318
# Total Accepted:    2.1M
# Total Submissions: 5.2M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    # def strStr(self, haystack: str, needle: str) -> int:
    #     if len(needle) > len(haystack):
    #         return -1
    #     for i in range(len(haystack)):
    #         if i + len(needle) > len(haystack):
    #             return -1

    #         if haystack[i : i + len(needle)] == needle:
    #             return i
    #     return -1


# @lc code=end
Solution().strStr("sadbutsad", "but")
