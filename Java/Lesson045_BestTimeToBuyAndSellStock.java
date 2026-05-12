// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 045 -- Best Time to Buy and Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given prices, return the maximum profit from a single buy/sell.
//
//   Example: [7,1,5,3,6,4] -> 5
// =============================================================

public class Lesson045_BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int lo = Integer.MAX_VALUE, best = 0;
        for (int p: prices) {
            if (p < lo) lo = p;
            else if (p - lo > best) best = p - lo;
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new Lesson045_BestTimeToBuyAndSellStock().maxProfit(new int[]{7,1,5,3,6,4}));
    }
}
