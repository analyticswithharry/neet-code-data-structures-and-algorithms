// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 174 -- Surrounded Regions
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).
// =============================================================
function solve(b){if(!b.length)return;const R=b.length,C=b[0].length;function dfs(r,c){if(r<0||r>=R||c<0||c>=C||b[r][c]!=='O')return;b[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}for(let r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(let c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(let r=0;r<R;r++)for(let c=0;c<C;c++)b[r][c]=b[r][c]==='S'?'O':'X';}
const g=[['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']];solve(g);console.log(g);
