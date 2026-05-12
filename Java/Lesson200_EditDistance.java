// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 200 -- Edit Distance
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Min number of insert/delete/replace ops to convert s1 to s2.
// =============================================================
public class Lesson200_EditDistance{
  static int minDistance(String a,String b){int m=a.length(),n=b.length();int[][] dp=new int[m+1][n+1];for(int i=0;i<=m;i++)dp[i][0]=i;for(int j=0;j<=n;j++)dp[0][j]=j;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(a.charAt(i-1)==b.charAt(j-1))dp[i][j]=dp[i-1][j-1];else dp[i][j]=1+Math.min(dp[i-1][j-1],Math.min(dp[i-1][j],dp[i][j-1]));}return dp[m][n];}
  public static void main(String[]a){System.out.println(minDistance("horse","ros"));System.out.println(minDistance("intention","execution"));}
}
