// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 018 -- Min Cost Climbing Stairs
// Category   : 1-D Dynamic Programming
// Difficulty : Easy
// Study Plan : Day 9
// =============================================================
//
// QUESTION:
//   You are given an integer array cost where cost[i] is the cost of i-th
//   step. Once you pay the cost, you can either climb one or two steps. You
//   can start from index 0 or 1. Return the minimum cost to reach the top.
//
//   Example:
//     Input : cost = [10,15,20]            Output: 15
//     Input : cost = [1,100,1,1,1,100,1,1,100,1]   Output: 6
// =============================================================

public class Lesson018_MinCostClimbingStairs {
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int c : cost) { int t = Math.min(a,b) + c; a = b; b = t; }
        return Math.min(a, b);
    }
    public static void main(String[] args) {
        Lesson018_MinCostClimbingStairs s = new Lesson018_MinCostClimbingStairs();
        System.out.println(s.minCostClimbingStairs(new int[]{10,15,20}) + " " +
                           s.minCostClimbingStairs(new int[]{1,100,1,1,1,100,1,1,100,1}));
    }
}
