# Given a positive integer n, generate an n x n matrix filled with elements 
# from 1 to n² in spiral order. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  
# 
#  👍 6186 👎 250
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def valid_index(matrix, x, y):
            if x < 0 or x >= n:
                return False
            if y < 0 or y >= n:
                return False
            return matrix[x][y] == 0

        matrix = [[0] * n for _ in range(n)]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move_index = 0
        x, y = 0, 0
        for i in range(1, n ** 2 + 1):
            matrix[x][y] = i
            move = moves[move_index]
            new_x, new_y = x + move[0], y + move[1]
            if not valid_index(matrix, new_x, new_y):
                move_index = (move_index + 1) % 4
                move = moves[move_index]
                new_x, new_y = x + move[0], y + move[1]
            x = new_x
            y = new_y
        return matrix

# leetcode submit region end(Prohibit modification and deletion)
Solution().generateMatrix(3)