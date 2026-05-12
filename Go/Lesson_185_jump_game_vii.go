//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 185 -- Jump Game VII
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?
// =============================================================
package main
import "fmt"
func canReach(s string,mn,mx int) bool { n:=len(s); if s[n-1]!='0'||s[0]!='0' { return false }; pre:=make([]int,n+1); r:=make([]bool,n); r[0]=true; pre[1]=1; for i:=1;i<n;i++ { if s[i]=='0' { lo:=i-mx; if lo<0 { lo=0 }; hi:=i-mn; if lo<=hi && pre[hi+1]-pre[lo]>0 { r[i]=true } }; v:=0; if r[i] { v=1 }; pre[i+1]=pre[i]+v }; return r[n-1] }
func main(){ fmt.Println(canReach("011010",2,3)); fmt.Println(canReach("01101110",2,3)) }
