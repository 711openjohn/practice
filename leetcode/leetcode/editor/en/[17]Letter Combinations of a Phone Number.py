# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digits to letters (just like on the telephone buttons) is given 
# below. Note that 1 does not map to any letters. 
#  
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
# 
#  👍 17772 👎 931
from typing import List

# time O(3^m * 4^n)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        lookup = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtracking(i, result, path):
            if len(path) == len(digits):
                result.append(''.join(path))
                return

            digit = digits[i]
            for c in lookup.get(digit):
                path.append(c)
                backtracking(i + 1, result, path)
                path.pop()

        result = []
        backtracking(0, result, [])

        return result

# leetcode submit region end(Prohibit modification and deletion)
Solution().letterCombinations('239')