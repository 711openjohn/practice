#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (46.43%)
# Likes:    7064
# Dislikes: 13821
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1:
            return s
        if numRows == 1:
            return s

        temp = [""] * numRows
        temp[0] += s[0]

        current = 1
        direction = 1
        for i in range(1, len(s)):
            temp[current] += s[i]
            mod = current % numRows
            if mod == numRows - 1:
                direction = direction * -1
            elif mod == 0:
                direction = direction * -1
            current += direction
        result = ""
        for t in temp:
            result += t
        return result

    # def convert(self, s: str, numRows: int) -> str:
    #     if len(s) == 0:
    #         return s
    #     if numRows == 1:
    #         return s

    #     result = []
    #     for _ in range(numRows):
    #         result.append([])

    #     direction = 1
    #     current = 1
    #     result[0].append(s[0])
    #     for idx, c in enumerate(s[1:]):
    #         result[current].append(c)
    #         if current == numRows - 1:
    #             direction = direction * -1
    #         if current == 0:
    #             direction = direction * -1
    #         current += direction
    #     converted = ''
    #     for r in result:
    #         converted += ''.join(r)
    #     return converted


# @lc code=end
Solution().convert("PAYPALISHIRING", 4)
