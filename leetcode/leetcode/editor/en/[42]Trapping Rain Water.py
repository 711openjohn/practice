# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  👍 30153 👎 448
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid_height = stack.pop()
                if stack:
                    # 雨水高度是 min(凹槽左侧高度, 凹槽右侧高度) - 凹槽底部高度
                    h = min(height[stack[-1]], height[i]) - height[mid_height]
                    # 雨水宽度是 凹槽右侧的下标 - 凹槽左侧的下标 - 1
                    w = i - stack[-1] - 1
                    # 累计总雨水体积
                    result += h * w
            stack.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])