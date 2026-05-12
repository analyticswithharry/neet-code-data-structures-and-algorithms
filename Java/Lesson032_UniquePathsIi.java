// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 032 -- Unique Paths II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 16
// =============================================================
//
// QUESTION:
//   You are given an m x n integer array obstacleGrid. There is a robot
//   at the top-left. It moves right or down. An obstacle is marked as 1; an
//   empty space as 0. Return the number of possible unique paths to the
//   bottom-right corner.
//
//   Example:
//     Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2
// =============================================================

public class Lesson032_UniquePathsIi {
    public int uniquePathsWithObstacles(int[][] g) {
        int R = g.length, C = g[0].length;
        if (g[0][0] == 1) return 0;
        int[] dp = new int[C]; dp[0] = 1;
        for (int r = 0; r < R; r++) {
            if (g[r][0] == 1) dp[0] = 0;
            for (int c = 1; c < C; c++) dp[c] = g[r][c] == 1 ? 0 : dp[c] + dp[c-1];
        }
        return dp[C-1];
    }
    public static void main(String[] args) {
        System.out.println(new Lesson032_UniquePathsIi().uniquePathsWithObstacles(new int[][]{{0,0,0},{0,1,0},{0,0,0}}));
    }
}
