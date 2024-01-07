# Given a string s, partition s such that every substring of the partition is a 
# palindrome. Return all possible palindrome partitioning of s. 
# 
#  
#  Example 1: 
#  Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#  
#  Example 2: 
#  Input: s = "a"
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s contains only lowercase English letters. 
#  
# 
#  👍 12062 👎 398
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(check):
            if len(check) == 0:
                return
            l = 0
            r = len(check) - 1
            while l <= r:
                if check[l] != check[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(result, path, start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                left = s[start:i + 1]
                if is_palindrome(left):
                    path.append(left)
                    backtracking(result, path, i + 1)
                    path.pop()

        result = []
        backtracking(result, [], 0)
        return result


# leetcode submit region end(Prohibit modification and deletion)
Solution().partition('aba')
