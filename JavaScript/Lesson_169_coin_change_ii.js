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
function change(amt,coins){const dp=new Array(amt+1).fill(0);dp[0]=1;for(const c of coins)for(let a=c;a<=amt;a++)dp[a]+=dp[a-c];return dp[amt];}
console.log(change(5,[1,2,5]));console.log(change(3,[2]));
