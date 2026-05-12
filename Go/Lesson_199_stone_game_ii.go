//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 199 -- Stone Game II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
// =============================================================
package main
import "fmt"
var SUF []int; var N int; var MEMO map[int]int
func dfs(i,m int) int { if i+2*m>=N { return SUF[i] }; k:=i*1000+m; if v,ok:=MEMO[k]; ok { return v }; best:=0; for x:=1;x<=2*m;x++ { mx:=m; if x>mx { mx=x }; v:=SUF[i]-dfs(i+x,mx); if v>best { best=v } }; MEMO[k]=best; return best }
func stoneGameII(p []int) int { N=len(p); SUF=make([]int,N+1); for i:=N-1;i>=0;i-- { SUF[i]=SUF[i+1]+p[i] }; MEMO=map[int]int{}; return dfs(0,1) }
func main(){ fmt.Println(stoneGameII([]int{2,7,9,4,4})) }
