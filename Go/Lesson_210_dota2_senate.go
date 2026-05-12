//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 210 -- Dota2 Senate
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
// =============================================================
package main
import "fmt"
func predictPartyVictory(s string) string { R,D:=[]int{},[]int{}; n:=len(s); for i:=0;i<n;i++ { if s[i]=='R' { R=append(R,i) } else { D=append(D,i) } }; for len(R)>0 && len(D)>0 { r:=R[0]; R=R[1:]; d:=D[0]; D=D[1:]; if r<d { R=append(R,r+n) } else { D=append(D,d+n) } }; if len(R)>0 { return "Radiant" }; return "Dire" }
func main(){ fmt.Println(predictPartyVictory("RD")); fmt.Println(predictPartyVictory("RDD")) }
