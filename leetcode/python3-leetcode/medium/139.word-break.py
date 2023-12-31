#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (46.38%)
# Likes:    16559
# Dislikes: 724
# Total Accepted:    1.6M
# Total Submissions: 3.4M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

from typing import List

# @lc code=start
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(1, len(s) + 1):
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (
                        dp[j - len(word)] and word == s[j - len(word) : j]
                    )
        return dp[len(s)]

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     n = len(s)
    #     dp = [False] * (n + 1)
    #     dp[0] = True
    #     for i in range(1, n + 1):
    #         for j in range(0, i):
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #     return dp[n]

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     n = len(s)
    #     dp = [False] * (n + 1)
    #     dp[0] = True

    #     for i in range(1, n + 1):
    #         for j in range(i):
    #             print(s[j:i])
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #     return dp[n]


# @lc code=end
# Solution().wordBreak("leetcode", ["leet", "code"])
Solution().wordBreak("applepenapple", ["apple", "pen"])
