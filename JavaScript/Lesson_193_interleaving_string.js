// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 193 -- Interleaving String
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Determine whether s3 can be formed by interleaving s1 and s2.
// =============================================================
function isInterleave(a,b,c){if(a.length+b.length!==c.length)return false;const dp=Array.from({length:a.length+1},()=>new Array(b.length+1).fill(false));dp[0][0]=true;for(let i=0;i<=a.length;i++)for(let j=0;j<=b.length;j++){if(i&&a[i-1]===c[i+j-1])dp[i][j]=dp[i][j]||dp[i-1][j];if(j&&b[j-1]===c[i+j-1])dp[i][j]=dp[i][j]||dp[i][j-1];}return dp[a.length][b.length];}
console.log(isInterleave("aabcc","dbbca","aadbbcbcac"));console.log(isInterleave("aabcc","dbbca","aadbbbaccc"));
