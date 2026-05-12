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
function coinChange(coins,amt){const INF=1e9;const dp=new Array(amt+1).fill(INF);dp[0]=0;for(let a=1;a<=amt;a++)for(const c of coins)if(c<=a)dp[a]=Math.min(dp[a],dp[a-c]+1);return dp[amt]===INF?-1:dp[amt];}
console.log(coinChange([1,2,5],11));console.log(coinChange([2],3));
