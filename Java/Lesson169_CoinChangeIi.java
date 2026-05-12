// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 169 -- Coin Change II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Number of distinct combinations of coins (unlimited) summing to amount.
// =============================================================
public class Lesson169_CoinChangeIi{
  static int change(int amt,int[] coins){int[] dp=new int[amt+1];dp[0]=1;for(int c:coins)for(int a=c;a<=amt;a++)dp[a]+=dp[a-c];return dp[amt];}
  public static void main(String[]a){System.out.println(change(5,new int[]{1,2,5}));System.out.println(change(3,new int[]{2}));}
}
