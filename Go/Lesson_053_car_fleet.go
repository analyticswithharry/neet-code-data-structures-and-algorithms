//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 053 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Cars at given positions move toward target with given speeds. A car
//   that catches up forms a fleet. Return the number of fleets that arrive.
//
//   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
// =============================================================

package main
import ("fmt"; "sort")
func carFleet(target int, position, speed []int) int {
    n := len(position); idx := make([]int, n)
    for i := range idx { idx[i] = i }
    sort.Slice(idx, func(i, j int) bool { return position[idx[i]] > position[idx[j]] })
    st := []float64{}
    for _, i := range idx {
        t := float64(target-position[i]) / float64(speed[i])
        if len(st)==0 || t > st[len(st)-1] { st = append(st, t) }
    }
    return len(st)
}
func main(){ fmt.Println(carFleet(12, []int{10,8,0,5,3}, []int{2,4,1,1,3})) }
