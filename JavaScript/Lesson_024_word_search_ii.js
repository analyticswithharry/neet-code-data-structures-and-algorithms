// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 024 -- Word Search II
// Category   : Tries
// Difficulty : Hard
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given an m x n board of characters and a list of strings words, return
//   all words on the board. Each word must be constructed from letters of
//   sequentially adjacent cells (horizontal/vertical). The same cell may not
//   be used more than once in a word.
//
//   Example:
//     board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
//     words=["oath","pea","eat","rain"]
//     Output: ["oath","eat"]
// =============================================================

var findWords = function(board, words) {
    const trie = {};
    for (const w of words) { let n = trie; for (const c of w) { n[c] = n[c] || {}; n = n[c]; } n['#'] = w; }
    const R = board.length, C = board[0].length, out = new Set();
    const dfs = (r, c, n) => {
        const ch = board[r][c];
        if (!n[ch]) return;
        const nxt = n[ch];
        if (nxt['#']) out.add(nxt['#']);
        board[r][c] = '*';
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (nr>=0&&nr<R&&nc>=0&&nc<C&&board[nr][nc]!=='*') dfs(nr,nc,nxt);
        }
        board[r][c] = ch;
    };
    for (let r=0;r<R;r++) for (let c=0;c<C;c++) dfs(r,c,trie);
    return [...out];
};
const b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]];
console.log(findWords(b, ["oath","pea","eat","rain"]).sort());
