# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  👍 17545 👎 622


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        n = len(nums)
        result = []
        for i in range(k):
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
        result.append(nums[d[0]])

        for i in range(k, n):
            if i - d[0] >= k:
                d.popleft()
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            result.append(nums[d[0]])
        return result
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     d = deque()
    #     n = len(nums)
    #     res = []
    #
    #     for i in range(k):
    #         while d and nums[d[-1]] <= nums[i]:
    #             d.pop()
    #         d.append(i)
    #     res.append(nums[d[0]])
    #
    #     for i in range(k, n):
    #         if i - d[0] >= k:
    #             d.popleft()
    #         while d and nums[d[-1]] <= nums[i]:
    #             d.pop()
    #         d.append(i)
    #         res.append(nums[d[0]])
    #     return res
# leetcode submit region end(Prohibit modification and deletion)
Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3)