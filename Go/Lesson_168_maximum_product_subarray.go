//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 168 -- Maximum Product Subarray
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Find a contiguous subarray with the largest product.
// =============================================================
package main
import "fmt"
func maxProduct(a []int) int { mx,mn,res:=a[0],a[0],a[0]; for i:=1;i<len(a);i++ { v:=a[i]; if v<0 { mx,mn=mn,mx }; if v>mx*v { mx=v } else { mx=mx*v }; if v<mn*v { mn=v } else { mn=mn*v }; if mx>res { res=mx } }; return res }
func main(){ fmt.Println(maxProduct([]int{2,3,-2,4})); fmt.Println(maxProduct([]int{-2,0,-1})) }
