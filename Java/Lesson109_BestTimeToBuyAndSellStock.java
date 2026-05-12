// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 109 -- Best Time to Buy And Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given an array of stock prices where prices[i] is on day i, return the maximum profit from a single buy/sell. Return 0 if none.
// =============================================================

public class Lesson109_BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices){
        int lo=Integer.MAX_VALUE, best=0;
        for (int p: prices){ lo=Math.min(lo,p); best=Math.max(best, p-lo); }
        return best;
    }
    public static void main(String[] a){ System.out.println(new Lesson109_BestTimeToBuyAndSellStock().maxProfit(new int[]{7,1,5,3,6,4})); }
}
