# You are given a list of airline tickets where tickets[i] = [fromi, toi] 
# represent the departure and the arrival airports of one flight. Reconstruct the 
# itinerary in order and return it. 
# 
#  All of the tickets belong to a man who departs from "JFK", thus, the 
# itinerary must begin with "JFK". If there are multiple valid itineraries, you should 
# return the itinerary that has the smallest lexical order when read as a single 
# string. 
# 
#  
#  For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than [
# "JFK", "LGB"]. 
#  
# 
#  You may assume all tickets form at least one valid itinerary. You must use 
# all the tickets once and only once. 
# 
#  
#  Example 1: 
#  
#  
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
#  
# 
#  Example 2: 
#  
#  
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],[
# "ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK",
# "ATL","SFO"] but it is larger in lexical order.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tickets.length <= 300 
#  tickets[i].length == 2 
#  fromi.length == 3 
#  toi.length == 3 
#  fromi and toi consist of uppercase English letters. 
#  fromi != toi 
#  
# 
#  👍 5722 👎 1839


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)  # 创建默认字典，用于存储机场映射关系
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])  # 将机票输入到字典中

        for key in targets:
            targets[key].sort(reverse=True)  # 对到达机场列表进行字母逆序排序

        result = []
        self.backtracking("JFK", targets, result)  # 调用回溯函数开始搜索路径
        return result[::-1]  # 返回逆序的行程路径

    def backtracking(self, airport, targets, result):
        while targets[airport]:  # 当机场还有可到达的机场时
            next_airport = targets[airport].pop()  # 弹出下一个机场
            self.backtracking(next_airport, targets, result)  # 递归调用回溯函数进行深度优先搜索
        result.append(airport)  # 将当前机场添加到行程路径中
# leetcode submit region end(Prohibit modification and deletion)
