# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
# of rows like this: (you may want to display this pattern in a fixed font for 
# better legibility) 
# 
#  
# P   A   H   N
# A P L S I I G
# Y   I   R
#  
# 
#  And then read line by line: "PAHNAPLSIIGYIR" 
# 
#  Write the code that will take a string and make this conversion given a 
# number of rows: 
# 
#  
# string convert(string s, int numRows);
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#  
# 
#  Example 2: 
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
#  Example 3: 
# 
#  
# Input: s = "A", numRows = 1
# Output: "A"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of English letters (lower-case and upper-case), ',' and '.'. 
#  1 <= numRows <= 1000 
#  
# 
#  👍 7121 👎 13921


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1:
            return s
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]
        move = 1
        index = 1
        zigzag[0].append(s[0])
        for c in s[1:]:
            zigzag[index].append(c)
            if index % numRows == 0 or index % numRows == numRows - 1:
                move = move * -1
            index += move
        result = ''
        for zig in zigzag:
            result += ''.join(zig)
        return result

# leetcode submit region end(Prohibit modification and deletion)
Solution().convert('AB', 1)