//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 186 -- Gas Station
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
// =============================================================
package main
import "fmt"
func canCompleteCircuit(g,c []int) int { s,t,tot:=0,0,0; for i:=0;i<len(g);i++ { d:=g[i]-c[i]; t+=d; tot+=d; if t<0 { s=i+1; t=0 } }; if tot<0 { return -1 }; return s }
func main(){ fmt.Println(canCompleteCircuit([]int{1,2,3,4,5},[]int{3,4,5,1,2})); fmt.Println(canCompleteCircuit([]int{2,3,4},[]int{3,4,3})) }
