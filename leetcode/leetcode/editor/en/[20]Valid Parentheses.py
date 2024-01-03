# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  👍 22992 👎 1607


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in close:
                if len(stack) == 0:
                    return False
                else:
                    left = stack.pop()
                    if close.get(c) != left:
                        return False
            else:
                stack.append(c)
        return len(stack) == 0
# leetcode submit region end(Prohibit modification and deletion)
Solution().isValid('(())[]}')