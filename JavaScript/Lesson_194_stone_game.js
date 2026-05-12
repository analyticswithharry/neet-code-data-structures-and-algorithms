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
function stoneGame(p){const n=p.length;const dp=Array.from({length:n},()=>new Array(n).fill(0));for(let i=0;i<n;i++)dp[i][i]=p[i];for(let L=2;L<=n;L++)for(let i=0;i<=n-L;i++){const j=i+L-1;dp[i][j]=Math.max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
console.log(stoneGame([5,3,4,5]));
