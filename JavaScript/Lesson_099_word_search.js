// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 099 -- Word Search
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Given an m x n board and a word, return true if the word exists by sequentially adjacent cells (no reuse).
// =============================================================

var exist = function(board, word){
  const R=board.length, C=board[0].length;
  const dfs=(r,c,i)=>{
    if (i===word.length) return true;
    if (r<0||r>=R||c<0||c>=C||board[r][c]!==word[i]) return false;
    const t=board[r][c]; board[r][c]='#';
    const ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
    board[r][c]=t; return ok;
  };
  for (let r=0;r<R;r++) for (let c=0;c<C;c++) if (dfs(r,c,0)) return true;
  return false;
};
console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"));
