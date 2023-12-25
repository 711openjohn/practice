#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (68.77%)
# Likes:    3406
# Dislikes: 281
# Total Accepted:    199.9K
# Total Submissions: 290.9K
# Testcase Example:  '["bella","label","roller"]'
#
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the
# answer in any order.
#
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
#
#
#


# @lc code=start
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        alist = set(words[0])  # make a set from first string
        res = []
        for one in alist:
            n = min(
                [a_word.count(one) for a_word in words]
            )  # count min frequency of every letter in every word
            if n:  # if n>0 , we append this letter n times
                res += [one] * n
        return res


# @lc code=end
Solution().commonChars(["bella", "label", "roller"])
