//go:build ignore

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
package main
import "fmt"
var R,C int; var G,M [][]int
func dfs(r,c int) int { if M[r][c]!=0 { return M[r][c] }; best:=1; for _,d:=range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} { nr,nc:=r+d[0],c+d[1]; if nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c] { v:=1+dfs(nr,nc); if v>best { best=v } } }; M[r][c]=best; return best }
func longestIncreasingPath(g [][]int) int { R=len(g); C=len(g[0]); G=g; M=make([][]int,R); for i:=range M { M[i]=make([]int,C) }; res:=0; for r:=0;r<R;r++ { for c:=0;c<C;c++ { v:=dfs(r,c); if v>res { res=v } } }; return res }
func main(){ fmt.Println(longestIncreasingPath([][]int{{9,9,4},{6,6,8},{2,1,1}})) }
