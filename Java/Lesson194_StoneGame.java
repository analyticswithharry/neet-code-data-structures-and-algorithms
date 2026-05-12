// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 194 -- Stone Game
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Two players take stones from either end. Both play optimally. Return true if Alice wins.
// =============================================================
public class Lesson194_StoneGame{
  static boolean stoneGame(int[] p){int n=p.length;int[][] dp=new int[n][n];for(int i=0;i<n;i++)dp[i][i]=p[i];for(int L=2;L<=n;L++)for(int i=0;i<=n-L;i++){int j=i+L-1;dp[i][j]=Math.max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
  public static void main(String[]a){System.out.println(stoneGame(new int[]{5,3,4,5}));}
}
