// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 202 -- Distinct Subsequences
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Number of distinct subsequences of s equal to t.
// =============================================================
public class Lesson202_DistinctSubsequences{
  static int numDistinct(String s,String t){int m=s.length(),n=t.length();long[][] dp=new long[m+1][n+1];for(int i=0;i<=m;i++)dp[i][0]=1;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){dp[i][j]=dp[i-1][j]+(s.charAt(i-1)==t.charAt(j-1)?dp[i-1][j-1]:0);}return (int)dp[m][n];}
  public static void main(String[]a){System.out.println(numDistinct("rabbbit","rabbit"));}
}
