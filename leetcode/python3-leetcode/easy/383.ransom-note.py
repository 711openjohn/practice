#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (60.03%)
# Likes:    4705
# Dislikes: 479
# Total Accepted:    983.6K
# Total Submissions: 1.6M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup = {}

        for m in magazine:
            lookup[m] = lookup.get(m, 0) + 1

        for r in ransomNote:
            current = lookup.get(r, 0)
            if current == 0:
                return False
            lookup[r] = current - 1
        return True


# @lc code=end
Solution().canConstruct("a", "b")
