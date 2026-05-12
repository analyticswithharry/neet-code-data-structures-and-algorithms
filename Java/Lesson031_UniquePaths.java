// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 031 -- Unique Paths
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   A robot is on an m x n grid at the top-left. It can only move right or
//   down. How many possible unique paths are there to reach the bottom-right?
//
//   Example:
//     Input : m=3, n=7  Output: 28
//     Input : m=3, n=2  Output: 3
// =============================================================

public class Lesson031_UniquePaths {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n]; java.util.Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) for (int j = 1; j < n; j++) dp[j] += dp[j-1];
        return dp[n-1];
    }
    public static void main(String[] args) {
        Lesson031_UniquePaths s = new Lesson031_UniquePaths();
        System.out.println(s.uniquePaths(3,7) + " " + s.uniquePaths(3,2));
    }
}
