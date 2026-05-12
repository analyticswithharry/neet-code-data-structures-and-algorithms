// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 173 -- Pacific Atlantic Water Flow
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).
// =============================================================
function pacificAtlantic(h){if(!h.length)return[];const R=h.length,C=h[0].length;const pac=Array.from({length:R},()=>new Array(C).fill(false));const atl=Array.from({length:R},()=>new Array(C).fill(false));function dfs(r,c,seen){seen[r][c]=true;for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){const nr=r+dr,nc=c+dc;if(nr>=0&&nr<R&&nc>=0&&nc<C&&!seen[nr][nc]&&h[nr][nc]>=h[r][c])dfs(nr,nc,seen);}}for(let c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(let r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}const res=[];for(let r=0;r<R;r++)for(let c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.push([r,c]);return res;}
console.log(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]).length);
