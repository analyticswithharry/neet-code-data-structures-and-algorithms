//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 045 -- Best Time to Buy and Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 22
// =============================================================
//
// QUESTION:
//   Given prices, return the maximum profit from a single buy/sell.
//
//   Example: [7,1,5,3,6,4] -> 5
// =============================================================

package main
import ("fmt"; "math")
func maxProfit(prices []int) int {
    lo := math.MaxInt32; best := 0
    for _,p := range prices {
        if p < lo { lo = p } else if p - lo > best { best = p - lo }
    }
    return best
}
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
