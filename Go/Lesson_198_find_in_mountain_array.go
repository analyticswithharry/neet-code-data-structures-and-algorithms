//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 198 -- Find in Mountain Array
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.
// =============================================================
package main
import "fmt"
func bs(a []int,l,r,t int,asc bool) int { for l<=r { m:=(l+r)/2; if a[m]==t { return m }; if asc { if a[m]<t { l=m+1 } else { r=m-1 } } else { if a[m]>t { l=m+1 } else { r=m-1 } } }; return -1 }
func findInMountainArray(t int,a []int) int { lo,hi:=0,len(a)-1; for lo<hi { m:=(lo+hi)/2; if a[m]<a[m+1] { lo=m+1 } else { hi=m } }; i:=bs(a,0,lo,t,true); if i!=-1 { return i }; return bs(a,lo+1,len(a)-1,t,false) }
func main(){ fmt.Println(findInMountainArray(3,[]int{1,2,3,4,5,3,1})) }
