// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 201 -- Longest Increasing Path In a Matrix
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Find length of the longest strictly-increasing path in a 2D grid.
// =============================================================
function longestIncreasingPath(g){if(!g.length)return 0;const R=g.length,C=g[0].length;const m=Array.from({length:R},()=>new Array(C).fill(0));function dfs(r,c){if(m[r][c])return m[r][c];let best=1;for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){const nr=r+dr,nc=c+dc;if(nr>=0&&nr<R&&nc>=0&&nc<C&&g[nr][nc]>g[r][c])best=Math.max(best,1+dfs(nr,nc));}m[r][c]=best;return best;}let res=0;for(let r=0;r<R;r++)for(let c=0;c<C;c++)res=Math.max(res,dfs(r,c));return res;}
console.log(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]));
