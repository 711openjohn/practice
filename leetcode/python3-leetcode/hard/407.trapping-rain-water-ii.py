#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (47.68%)
# Likes:    3652
# Dislikes: 89
# Total Accepted:    84.3K
# Total Submissions: 176.7K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n integer matrix heightMap representing the height of each unit
# cell in a 2D elevation map, return the volume of water it can trap after
# raining.
# 
# 
# Example 1:
# 
# 
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# 
# 
# Example 2:
# 
# 
# Input: heightMap =
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
# 
# 
# 
# Constraints:
# 
# 
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
# @lc code=end

