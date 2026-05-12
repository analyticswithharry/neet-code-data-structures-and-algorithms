//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 033 -- Last Stone Weight
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   You are given an array of stones. On each turn pick the two heaviest
//   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
//   and y becomes y - x. Return the weight of the last remaining stone (or 0).
//
//   Example:
//     Input : [2,7,4,1,8,1]   Output: 1
// =============================================================

package main
import ("container/heap"; "fmt")
type IH []int
func (h IH) Len() int { return len(h) }
func (h IH) Less(i,j int) bool { return h[i] > h[j] }
func (h IH) Swap(i,j int) { h[i], h[j] = h[j], h[i] }
func (h *IH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IH) Pop() interface{} { o := *h; n := len(o); x := o[n-1]; *h = o[:n-1]; return x }
func lastStoneWeight(stones []int) int {
    h := IH(append([]int{}, stones...)); heap.Init(&h)
    for h.Len() > 1 {
        y := heap.Pop(&h).(int); x := heap.Pop(&h).(int)
        if y != x { heap.Push(&h, y-x) }
    }
    if h.Len() == 0 { return 0 }
    return h[0]
}
func main() { fmt.Println(lastStoneWeight([]int{2,7,4,1,8,1})) }
