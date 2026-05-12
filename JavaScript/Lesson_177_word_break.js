// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 177 -- Word Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Determine if string s can be segmented into words from the given dictionary.
// =============================================================
function wordBreak(s,wd){const w=new Set(wd);const n=s.length;const dp=new Array(n+1).fill(false);dp[0]=true;for(let i=1;i<=n;i++)for(let j=0;j<i;j++)if(dp[j]&&w.has(s.substring(j,i))){dp[i]=true;break;}return dp[n];}
console.log(wordBreak("leetcode",["leet","code"]));console.log(wordBreak("catsandog",["cats","dog","sand","and","cat"]));
