# You are given a string s. We want to partition the string into as many parts 
# as possible so that each letter appears in at most one part. 
# 
#  Note that the partition is done so that after concatenating all the parts in 
# order, the resultant string should be s. 
# 
#  Return a list of integers representing the size of these parts. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits s into less parts.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "eccbbbbdec"
# Output: [10]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of lowercase English letters. 
#  
# 
#  👍 10074 👎 373
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
        result = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_index[s[i]])
            if end == i:
                result.append(i - start + 1)
                start = i + 1
        return result

    # def partitionLabels(self, s: str) -> List[int]:
    #     last_occurrence = {}  # 存储每个字符最后出现的位置
    #     for i, ch in enumerate(s):
    #         last_occurrence[ch] = i
    #
    #     result = []
    #     start = 0
    #     end = 0
    #     for i, ch in enumerate(s):
    #         end = max(end, last_occurrence[ch])  # 找到当前字符出现的最远位置
    #         if i == end:  # 如果当前位置是最远位置，表示可以分割出一个区间
    #             result.append(end - start + 1)
    #             start = i + 1
    #
    #     return result
# leetcode submit region end(Prohibit modification and deletion)
