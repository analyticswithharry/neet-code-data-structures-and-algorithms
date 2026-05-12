// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 102 -- Longest Common Subsequence
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given two strings text1 and text2, return the length of their longest common subsequence.
// =============================================================

public class Lesson102_LongestCommonSubsequence {
    public int longestCommonSubsequence(String a, String b){
        int m=a.length(), n=b.length();
        int[][] dp=new int[m+1][n+1];
        for (int i=0;i<m;i++) for (int j=0;j<n;j++){
            if (a.charAt(i)==b.charAt(j)) dp[i+1][j+1]=dp[i][j]+1;
            else dp[i+1][j+1]=Math.max(dp[i][j+1], dp[i+1][j]);
        }
        return dp[m][n];
    }
    public static void main(String[] a){
        System.out.println(new Lesson102_LongestCommonSubsequence().longestCommonSubsequence("abcde","ace"));
    }
}
