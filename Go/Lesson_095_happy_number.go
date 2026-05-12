//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 095 -- Happy Number
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
// =============================================================

package main
import "fmt"
func isHappy(n int) bool {
    seen := map[int]bool{}
    for n != 1 && !seen[n] {
        seen[n] = true; s := 0
        for n > 0 { d := n%10; s += d*d; n /= 10 }
        n = s
    }
    return n == 1
}
func main(){ fmt.Println(isHappy(19), isHappy(2)) }
