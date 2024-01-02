# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the 
# histogram. 
# 
#  
#  Example 1: 
#  
#  
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#  
# 
#  Example 2: 
#  
#  
# Input: heights = [2,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= heights.length <= 10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  👍 16418 👎 241
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1,len(heights)):
            # 情况一
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            # 情况二
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # 情况三
            else:
                # 抛出所有较高的柱子
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈顶就是中间的柱子，主心骨
                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        width = right_index - left_index - 1
                        height = heights[mid_index]
                        result = max(result, width * height)
                stack.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)

Solution().largestRectangleArea([2,1,5,6,2,3])