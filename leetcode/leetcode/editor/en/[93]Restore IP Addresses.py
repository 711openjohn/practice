# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros. 
# 
#  
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
#  
# 
#  Given a string s containing only digits, return all possible valid IP 
# addresses that can be formed by inserting dots into s. You are not allowed to reorder 
# or remove any digits in s. You may return the valid IP addresses in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "0000"
# Output: ["0.0.0.0"]
#  
# 
#  Example 3: 
# 
#  
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  s consists of digits only. 
#  
# 
#  👍 5050 👎 776
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(s: str):
            if len(s) > 1 and s.startswith('0'):
                return False
            if s.isdigit():
                if 0 <= int(s) < 256:
                    return True
            return False
        def backtracking(result, path, start):
            if start == len(s):
                if len(path) == 4:
                    result.append('.'.join(path))
                return

            for i in range(start, start + 3):
                if i >= len(s):
                    continue
                if len(s) - i > 3 * (4 - len(path)):
                    continue
                if len(s) - i < 4 - len(path):
                    continue

                candidate = s[start: i + 1]
                if is_valid(candidate):
                    path.append(candidate)
                    backtracking(result, path, i + 1)
                    path.pop()
        result = []
        backtracking(result, [], 0)
        return result

# leetcode submit region end(Prohibit modification and deletion)
Solution().restoreIpAddresses('101023')