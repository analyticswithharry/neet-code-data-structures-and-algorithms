//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 192 -- Word Break II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return all sentences obtainable by segmenting s using words from dict.
// =============================================================
package main
import "fmt"
var M map[int][]string; var S string; var W map[string]bool
func dfs(i int) []string { if i==len(S) { return []string{""} }; if v,ok:=M[i]; ok { return v }; var out []string; for j:=i+1;j<=len(S);j++ { p:=S[i:j]; if W[p] { for _,t:=range dfs(j) { if t=="" { out=append(out,p) } else { out=append(out,p+" "+t) } } } }; M[i]=out; return out }
func wordBreak(s string,wd []string) []string { M=map[int][]string{}; S=s; W=map[string]bool{}; for _,x:=range wd { W[x]=true }; return dfs(0) }
func main(){ fmt.Println(wordBreak("catsanddog",[]string{"cat","cats","and","sand","dog"})) }
