//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 161 -- Pow x n
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Implement pow(x, n) — x raised to the n-th power.
// =============================================================
package main
import "fmt"
func myPow(x float64,n int) float64 { if n<0 { x=1/x; n=-n }; r:=1.0; for n>0 { if n&1==1 { r*=x }; x*=x; n>>=1 }; return r }
func main(){ fmt.Println(myPow(2,10)); fmt.Println(myPow(2,-2)) }
