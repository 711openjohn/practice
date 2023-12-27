#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.50%)
# Likes:    11453
# Dislikes: 363
# Total Accepted:    3M
# Total Submissions: 4.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        for c in s:
            cache[c] = cache.get(c, 0) + 1
        for c in t:
            cache[c] = cache.get(c, 0) - 1

        for v in cache.values():
            if v != 0:
                return False
        return True

    # def isAnagram(self, s: str, t: str) -> bool:
    #     count = {}
    #     for c in s:
    #         count[c] = count.get(c, 0) + 1

    #     for c in t:
    #         count[c] = count.get(c, 0) - 1

    #     for v in count.values():
    #         if v != 0:
    #             return False
    #     return True


# @lc code=end
