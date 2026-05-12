//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 060 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 30
// =============================================================
//
// QUESTION:
//   Given two sorted arrays nums1 and nums2, return the median of the
//   combined sorted array. Run in O(log(min(m,n))).
//
//   Example: [1,3], [2] -> 2.0
// =============================================================

package main
import ("fmt"; "math")
func findMedianSortedArrays(a, b []int) float64 {
    if len(a) > len(b) { a, b = b, a }
    m, n := len(a), len(b); half := (m+n+1)/2
    lo, hi := 0, m
    max := func(x,y int) int { if x>y {return x}; return y }
    min := func(x,y int) int { if x<y {return x}; return y }
    for lo <= hi {
        i := (lo+hi)/2; j := half - i
        la := math.MinInt32; if i>0 { la = a[i-1] }
        ra := math.MaxInt32; if i<m { ra = a[i] }
        lb := math.MinInt32; if j>0 { lb = b[j-1] }
        rb := math.MaxInt32; if j<n { rb = b[j] }
        if la <= rb && lb <= ra {
            if (m+n) % 2 == 1 { return float64(max(la, lb)) }
            return float64(max(la, lb) + min(ra, rb)) / 2.0
        } else if la > rb { hi = i-1 } else { lo = i+1 }
    }
    return 0
}
func main(){
    fmt.Println(findMedianSortedArrays([]int{1,3}, []int{2}))
    fmt.Println(findMedianSortedArrays([]int{1,2}, []int{3,4}))
}
