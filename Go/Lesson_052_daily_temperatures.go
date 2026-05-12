//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 052 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Given temperatures, for each day return the number of days until a
//   warmer temperature, or 0 if none.
//
//   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
// =============================================================

package main
import "fmt"
func dailyTemperatures(t []int) []int {
    n := len(t); res := make([]int, n); st := []int{}
    for i:=0;i<n;i++ {
        for len(st)>0 && t[st[len(st)-1]] < t[i] {
            j := st[len(st)-1]; st = st[:len(st)-1]; res[j] = i - j
        }
        st = append(st, i)
    }
    return res
}
func main(){ fmt.Println(dailyTemperatures([]int{73,74,75,71,69,72,76,73})) }
