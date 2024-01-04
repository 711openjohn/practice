# Given a string array words, return an array of all characters that show up in 
# all strings within the words (including duplicates). You may return the answer 
# in any order. 
# 
#  
#  Example 1: 
#  Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
#  
#  Example 2: 
#  Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 100 
#  words[i] consists of lowercase English letters. 
#  
# 
#  👍 3414 👎 283
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        def to_freq(word):
            freq = {}
            for c in word:
                freq[c] = freq.get(c, 0) + 1
            return freq

        result_freq = to_freq(words[0])
        for i in range(1, len(words)):
            temp = to_freq(words[i])
            keys = set(result_freq.keys()).intersection(set(temp.keys()))
            new_result = {}
            for k in keys:
                new_result[k] = min(temp[k], result_freq[k])
            result_freq = new_result
        result = []
        for k, v in result_freq.items():
            for i in range(v):
                result.append(k)
        return result
# leetcode submit region end(Prohibit modification and deletion)

Solution().commonChars(["bella","label","roller"])