//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 207 -- Decode String
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
// =============================================================
package main
import ("fmt"; "strings")
func decodeString(s string) string { type fr struct{ pre string; k int }; st:=[]fr{}; cur:=""; k:=0; for _,ch:=range s { if ch>='0'&&ch<='9' { k=k*10+int(ch-'0') } else if ch=='[' { st=append(st,fr{cur,k}); cur=""; k=0 } else if ch==']' { f:=st[len(st)-1]; st=st[:len(st)-1]; cur=f.pre+strings.Repeat(cur,f.k) } else { cur+=string(ch) } }; return cur }
func main(){ fmt.Println(decodeString("3[a]2[bc]")); fmt.Println(decodeString("3[a2[c]]")) }
