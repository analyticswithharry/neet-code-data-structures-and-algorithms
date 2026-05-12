# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 018 -- Min Cost Climbing Stairs
# Category   : 1-D Dynamic Programming
# Difficulty : Easy
# Study Plan : Day 9
# =============================================================
#
# QUESTION:
#   You are given an integer array cost where cost[i] is the cost of i-th
#   step. Once you pay the cost, you can either climb one or two steps. You
#   can start from index 0 or 1. Return the minimum cost to reach the top.
#
#   Example:
#     Input : cost = [10,15,20]            Output: 15
#     Input : cost = [1,100,1,1,1,100,1,1,100,1]   Output: 6
# =============================================================

class Solution:
    def minCostClimbingStairs(self, cost):
        a = b = 0
        for c in cost: a, b = b, min(a, b) + c
        return min(a, b)

if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]), s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
