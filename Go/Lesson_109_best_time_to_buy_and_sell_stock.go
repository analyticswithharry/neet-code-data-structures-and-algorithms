//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 109 -- Best Time to Buy And Sell Stock
// Category   : Sliding Window
// Difficulty : Easy
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given an array of stock prices where prices[i] is on day i, return the maximum profit from a single buy/sell. Return 0 if none.
// =============================================================

package main
import ( "fmt"; "math" )
func maxProfit(prices []int) int {
    lo, best := math.MaxInt32, 0
    for _, p := range prices { if p<lo{lo=p}; if p-lo>best{best=p-lo} }
    return best
}
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
