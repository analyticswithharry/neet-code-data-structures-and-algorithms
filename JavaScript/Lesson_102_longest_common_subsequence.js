// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 102 -- Longest Common Subsequence
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 51
// =============================================================
//
// QUESTION:
//   Given two strings text1 and text2, return the length of their longest common subsequence.
// =============================================================

var longestCommonSubsequence = function(a, b){
  const m=a.length, n=b.length;
  const dp=Array.from({length:m+1},()=>Array(n+1).fill(0));
  for (let i=0;i<m;i++) for (let j=0;j<n;j++){
    if (a[i]===b[j]) dp[i+1][j+1]=dp[i][j]+1;
    else dp[i+1][j+1]=Math.max(dp[i][j+1], dp[i+1][j]);
  }
  return dp[m][n];
};
console.log(longestCommonSubsequence("abcde","ace"));
