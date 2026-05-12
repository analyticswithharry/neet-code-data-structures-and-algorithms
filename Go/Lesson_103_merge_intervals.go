//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 103 -- Merge Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
// =============================================================

package main
import ( "fmt"; "sort" )
func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i,j int) bool { return intervals[i][0] < intervals[j][0] })
    res := [][]int{}
    for _, x := range intervals {
        if n := len(res); n > 0 && x[0] <= res[n-1][1] { if x[1] > res[n-1][1] { res[n-1][1] = x[1] }
        } else { res = append(res, []int{x[0], x[1]}) }
    }
    return res
}
func main(){ fmt.Println(merge([][]int{{1,3},{2,6},{8,10},{15,18}})) }
