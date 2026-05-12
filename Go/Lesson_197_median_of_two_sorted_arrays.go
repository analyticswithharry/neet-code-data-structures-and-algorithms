//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 197 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Find the median of the two sorted arrays in O(log(min(m,n))).
// =============================================================
package main
import ("fmt"; "math")
func findMedianSortedArrays(a,b []int) float64 { if len(a)>len(b) { a,b=b,a }; m,n:=len(a),len(b); lo,hi:=0,m; for lo<=hi { i:=(lo+hi)/2; j:=(m+n+1)/2-i; Lx:=math.MinInt32; if i>0 { Lx=a[i-1] }; Rx:=math.MaxInt32; if i<m { Rx=a[i] }; Ly:=math.MinInt32; if j>0 { Ly=b[j-1] }; Ry:=math.MaxInt32; if j<n { Ry=b[j] }; if Lx<=Ry && Ly<=Rx { mx:=Lx; if Ly>mx { mx=Ly }; if (m+n)%2==1 { return float64(mx) }; mn:=Rx; if Ry<mn { mn=Ry }; return (float64(mx)+float64(mn))/2.0 } else if Lx>Ry { hi=i-1 } else { lo=i+1 } }; return 0 }
func main(){ fmt.Println(findMedianSortedArrays([]int{1,3},[]int{2})); fmt.Println(findMedianSortedArrays([]int{1,2},[]int{3,4})) }
