//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 177 -- Word Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Determine if string s can be segmented into words from the given dictionary.
// =============================================================
package main
import "fmt"
func wordBreak(s string,wd []string) bool { w:=map[string]bool{}; for _,x:=range wd { w[x]=true }; n:=len(s); dp:=make([]bool,n+1); dp[0]=true; for i:=1;i<=n;i++ { for j:=0;j<i;j++ { if dp[j] && w[s[j:i]] { dp[i]=true; break } } }; return dp[n] }
func main(){ fmt.Println(wordBreak("leetcode",[]string{"leet","code"})); fmt.Println(wordBreak("catsandog",[]string{"cats","dog","sand","and","cat"})) }
