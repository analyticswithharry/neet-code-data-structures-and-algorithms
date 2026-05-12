//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 019 -- Kth Largest Element In a Stream
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Design a class to find the kth largest element in a stream. Implement:
//     KthLargest(int k, int[] nums)
//     add(val) -> returns the element representing the kth largest in the stream.
//
//   Example:
//     k=3, nums=[4,5,8,2]
//     add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
// =============================================================

package main
import ("container/heap"; "fmt")
type IntHeap []int
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i,j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i,j int) { h[i],h[j] = h[j],h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type KthLargest struct { h *IntHeap; k int }
func Constructor(k int, nums []int) KthLargest {
    h := &IntHeap{}; heap.Init(h)
    kl := KthLargest{h, k}
    for _, n := range nums { kl.Add(n) }
    return kl
}
func (kl *KthLargest) Add(val int) int {
    if kl.h.Len() < kl.k { heap.Push(kl.h, val)
    } else if val > (*kl.h)[0] { heap.Pop(kl.h); heap.Push(kl.h, val) }
    return (*kl.h)[0]
}

func main() {
    kl := Constructor(3, []int{4,5,8,2})
    for _, x := range []int{3,5,10,9,4} { fmt.Print(kl.Add(x), " ") }
    fmt.Println()
}
