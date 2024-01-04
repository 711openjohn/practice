# Given three integer arrays nums1, nums2, and nums3, return a distinct array 
# containing all the values that are present
# in at least two out of the three
# arrays. You may return the values in any order.
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length, nums3.length <= 100 
#  1 <= nums1[i], nums2[j], nums3[k] <= 100 
#  
# 
#  👍 713 👎 46
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all = set()
        s1 = set()
        s2 = set()
        s3 = set()
        for n in nums1:
            all.add(n)
            s1.add(n)
        for n in nums2:
            all.add(n)
            s2.add(n)
        for n in nums3:
            all.add(n)
            s3.add(n)
        result = []
        for i in all:
            count = 0
            if i in s1:
                count += 1
            if i in s2:
                count += 1
            if i in s3:
                count += 1
            if count > 1:
                result.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().twoOutOfThree([1,1,3,2],[2,3],[3])