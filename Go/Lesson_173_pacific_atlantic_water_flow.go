//go:build ignore

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
package main
import "fmt"
func pacificAtlantic(h [][]int) [][]int { if len(h)==0 { return nil }; R,C:=len(h),len(h[0]); pac:=make([][]bool,R); atl:=make([][]bool,R); for i:=range pac { pac[i]=make([]bool,C); atl[i]=make([]bool,C) }; var dfs func(r,c int,s [][]bool); dfs=func(r,c int,s [][]bool){ s[r][c]=true; for _,d:=range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} { nr,nc:=r+d[0],c+d[1]; if nr>=0 && nr<R && nc>=0 && nc<C && !s[nr][nc] && h[nr][nc]>=h[r][c] { dfs(nr,nc,s) } } }; for c:=0;c<C;c++ { dfs(0,c,pac); dfs(R-1,c,atl) }; for r:=0;r<R;r++ { dfs(r,0,pac); dfs(r,C-1,atl) }; var res [][]int; for r:=0;r<R;r++ { for c:=0;c<C;c++ { if pac[r][c] && atl[r][c] { res=append(res,[]int{r,c}) } } }; return res }
func main(){ fmt.Println(len(pacificAtlantic([][]int{{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}))) }
