//go:build ignore

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
package main
import "fmt"
func solve(b [][]byte){ if len(b)==0 { return }; R,C:=len(b),len(b[0]); var dfs func(r,c int); dfs=func(r,c int){ if r<0||r>=R||c<0||c>=C||b[r][c]!='O' { return }; b[r][c]='S'; dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1) }; for r:=0;r<R;r++ { dfs(r,0); dfs(r,C-1) }; for c:=0;c<C;c++ { dfs(0,c); dfs(R-1,c) }; for r:=0;r<R;r++ { for c:=0;c<C;c++ { if b[r][c]=='S' { b[r][c]='O' } else { b[r][c]='X' } } } }
func main(){ g:=[][]byte{[]byte("XXXX"),[]byte("XOOX"),[]byte("XXOX"),[]byte("XOXX")}; solve(g); for _,r:=range g { fmt.Println(string(r)) } }
