//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 104 -- Non Overlapping Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
// =============================================================

package main
import ( "fmt"; "math"; "sort" )
func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i,j int) bool { return intervals[i][1] < intervals[j][1] })
    end, rm := math.MinInt32, 0
    for _, x := range intervals { if x[0] >= end { end = x[1] } else { rm++ } }
    return rm
}
func main(){ fmt.Println(eraseOverlapIntervals([][]int{{1,2},{2,3},{3,4},{1,3}})) }
