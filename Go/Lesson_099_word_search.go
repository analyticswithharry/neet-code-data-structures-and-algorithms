//go:build ignore

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

package main
import "fmt"
func exist(board [][]byte, word string) bool {
    R, C := len(board), len(board[0])
    var dfs func(r,c,i int) bool
    dfs = func(r,c,i int) bool {
        if i == len(word) { return true }
        if r<0||r>=R||c<0||c>=C||board[r][c]!=word[i] { return false }
        t := board[r][c]; board[r][c] = '#'
        ok := dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1)
        board[r][c] = t; return ok
    }
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { if dfs(r,c,0) { return true } } }
    return false
}
func main(){ b := [][]byte{[]byte("ABCE"), []byte("SFCS"), []byte("ADEE")}; fmt.Println(exist(b, "ABCCED")) }
