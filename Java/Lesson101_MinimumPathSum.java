// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 101 -- Minimum Path Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).
// =============================================================

public class Lesson101_MinimumPathSum {
    public int minPathSum(int[][] g){
        int R=g.length, C=g[0].length;
        for (int i=0;i<R;i++) for (int j=0;j<C;j++){
            if (i==0 && j==0) continue;
            if (i==0) g[i][j]+=g[i][j-1];
            else if (j==0) g[i][j]+=g[i-1][j];
            else g[i][j]+=Math.min(g[i-1][j], g[i][j-1]);
        }
        return g[R-1][C-1];
    }
    public static void main(String[] a){
        System.out.println(new Lesson101_MinimumPathSum().minPathSum(new int[][]{{1,3,1},{1,5,1},{4,2,1}}));
    }
}
