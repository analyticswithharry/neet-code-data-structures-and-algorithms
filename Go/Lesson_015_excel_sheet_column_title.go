//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 015 -- Excel Sheet Column Title
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   Given an integer columnNumber, return its corresponding column title
//   as it appears in an Excel sheet.
//
//   Example:
//     1  -> A
//     28 -> AB
//     701 -> ZY
// =============================================================

package main
import "fmt"
func convertToTitle(n int) string {
    out := []byte{}
    for n > 0 { n--; out = append([]byte{byte('A' + n%26)}, out...); n /= 26 }
    return string(out)
}
func main() { fmt.Println(convertToTitle(1), convertToTitle(28), convertToTitle(701)) }
