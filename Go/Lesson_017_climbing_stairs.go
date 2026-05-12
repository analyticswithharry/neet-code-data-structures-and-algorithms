//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 017 -- Climbing Stairs
// Category   : 1-D Dynamic Programming
// Difficulty : Easy
// Study Plan : Day 9
// =============================================================
//
// QUESTION:
//   You are climbing a staircase. It takes n steps to reach the top. Each
//   time you can climb 1 or 2 steps. In how many distinct ways can you climb
//   to the top?
//
//   Example:
//     Input : n = 2  -> 2
//     Input : n = 3  -> 3
// =============================================================

package main
import "fmt"
func climbStairs(n int) int {
    a, b := 1, 1
    for i := 0; i < n; i++ { a, b = b, a+b }
    return a
}
func main() { fmt.Println(climbStairs(2), climbStairs(3), climbStairs(5)) }
