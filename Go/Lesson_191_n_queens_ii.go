//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 191 -- N Queens II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return number of distinct solutions for n-queens.
// =============================================================
package main
import "fmt"
func totalNQueens(n int) int { cnt:=0; c:=map[int]bool{}; d1:=map[int]bool{}; d2:=map[int]bool{}; var bt func(r int); bt=func(r int){ if r==n { cnt++; return }; for i:=0;i<n;i++ { if c[i]||d1[r-i]||d2[r+i] { continue }; c[i]=true; d1[r-i]=true; d2[r+i]=true; bt(r+1); delete(c,i); delete(d1,r-i); delete(d2,r+i) } }; bt(0); return cnt }
func main(){ fmt.Println(totalNQueens(4)); fmt.Println(totalNQueens(8)) }
