# An integer has monotone increasing digits if and only if each pair of 
# adjacent digits x and y satisfy x <= y. 
# 
#  Given an integer n, return the largest number that is less than or equal to 
# n with monotone increasing digits. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 9
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1234
# Output: 1234
#  
# 
#  Example 3: 
# 
#  
# Input: n = 332
# Output: 299
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  👍 1282 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        result = list(str(n))
        for i in range(len(result) - 1, 0, -1):
            if result[i - 1] > result[i]:
                result[i - 1] = str(int(result[i - 1]) - 1)
                for j in range(i, len(result)):
                    result[j] = '9'
        return int(''.join(result))
    # def monotoneIncreasingDigits(self, n: int) -> int:
    #     strNum = list(str(n))
    #     for i in range(len(strNum) - 1, 0, -1):
    #         # 如果当前字符比前一个字符小，说明需要修改前一个字符
    #         if strNum[i - 1] > strNum[i]:
    #             strNum[i - 1] = str(int(strNum[i - 1]) - 1)  # 将前一个字符减1
    #             # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
    #             for j in range(i, len(strNum)):
    #                 strNum[j] = '9'
    #
    #         # 将列表转换为字符串，并将字符串转换为整数并返回
    #     return int(''.join(strNum))


# leetcode submit region end(Prohibit modification and deletion)
Solution().monotoneIncreasingDigits(100)
