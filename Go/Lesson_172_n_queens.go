//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 172 -- N Queens
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
// =============================================================
package main
import "fmt"
func totalNQueens(n int) int { cnt:=0; cols:=map[int]bool{}; d1:=map[int]bool{}; d2:=map[int]bool{}; var bt func(r int); bt=func(r int){ if r==n { cnt++; return }; for c:=0;c<n;c++ { if cols[c]||d1[r-c]||d2[r+c] { continue }; cols[c]=true; d1[r-c]=true; d2[r+c]=true; bt(r+1); delete(cols,c); delete(d1,r-c); delete(d2,r+c) } }; bt(0); return cnt }
func main(){ fmt.Println(totalNQueens(4)); fmt.Println(totalNQueens(6)) }
