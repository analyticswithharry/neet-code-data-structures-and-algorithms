// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 167 -- Coin Change
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.
// =============================================================
import java.util.*;
public class Lesson167_CoinChange{
  static int coinChange(int[] coins,int amt){int INF=Integer.MAX_VALUE/2;int[] dp=new int[amt+1];Arrays.fill(dp,INF);dp[0]=0;for(int a=1;a<=amt;a++)for(int c:coins)if(c<=a)dp[a]=Math.min(dp[a],dp[a-c]+1);return dp[amt]>=INF?-1:dp[amt];}
  public static void main(String[]a){System.out.println(coinChange(new int[]{1,2,5},11));System.out.println(coinChange(new int[]{2},3));}
}
