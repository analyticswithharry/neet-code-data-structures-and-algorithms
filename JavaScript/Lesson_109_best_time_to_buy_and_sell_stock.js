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

var maxProfit = function(prices){
  let lo=Infinity, best=0;
  for (const p of prices){ lo=Math.min(lo,p); best=Math.max(best, p-lo); }
  return best;
};
console.log(maxProfit([7,1,5,3,6,4]));
