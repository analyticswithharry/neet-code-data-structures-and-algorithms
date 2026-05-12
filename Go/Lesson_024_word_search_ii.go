//go:build ignore

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

package main
import ("fmt"; "sort")
type Node struct { ch map[byte]*Node; word string }
func newNode() *Node { return &Node{ch: map[byte]*Node{}} }
func findWords(board [][]byte, words []string) []string {
    root := newNode()
    for _, w := range words {
        n := root
        for i := 0; i < len(w); i++ {
            c := w[i]
            if _, ok := n.ch[c]; !ok { n.ch[c] = newNode() }
            n = n.ch[c]
        }
        n.word = w
    }
    R, C := len(board), len(board[0])
    out := map[string]bool{}
    var dfs func(r, c int, n *Node)
    dfs = func(r, c int, n *Node) {
        ch := board[r][c]
        nxt, ok := n.ch[ch]; if !ok { return }
        if nxt.word != "" { out[nxt.word] = true }
        board[r][c] = '*'
        for _, d := range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} {
            nr, nc := r+d[0], c+d[1]
            if nr>=0 && nr<R && nc>=0 && nc<C && board[nr][nc] != '*' { dfs(nr, nc, nxt) }
        }
        board[r][c] = ch
    }
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { dfs(r, c, root) } }
    res := []string{}
    for k := range out { res = append(res, k) }
    sort.Strings(res)
    return res
}
func main() {
    b := [][]byte{[]byte("oaan"), []byte("etae"), []byte("ihkr"), []byte("iflv")}
    fmt.Println(findWords(b, []string{"oath","pea","eat","rain"}))
}
