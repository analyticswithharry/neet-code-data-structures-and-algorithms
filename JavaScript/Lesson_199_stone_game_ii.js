// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 199 -- Stone Game II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
// =============================================================
function stoneGameII(p){const n=p.length;const suf=new Array(n+1).fill(0);for(let i=n-1;i>=0;i--)suf[i]=suf[i+1]+p[i];const memo=new Map();function dfs(i,M){if(i+2*M>=n)return suf[i];const k=i*100+M;if(memo.has(k))return memo.get(k);let best=0;for(let x=1;x<=2*M;x++)best=Math.max(best,suf[i]-dfs(i+x,Math.max(M,x)));memo.set(k,best);return best;}return dfs(0,1);}
console.log(stoneGameII([2,7,9,4,4]));
