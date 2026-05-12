//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 100 -- Palindrome Partitioning
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Partition string s such that every substring is a palindrome. Return all possible partitions.
// =============================================================

package main
import "fmt"
func partition(s string) [][]string {
    var res [][]string; cur := []string{}
    isPal := func(x string) bool { for i,j:=0,len(x)-1; i<j; i,j=i+1,j-1 { if x[i]!=x[j] { return false } }; return true }
    var bt func(int)
    bt = func(i int){
        if i == len(s) { tmp := make([]string, len(cur)); copy(tmp, cur); res = append(res, tmp); return }
        for j := i+1; j <= len(s); j++ {
            sub := s[i:j]; if isPal(sub) { cur = append(cur, sub); bt(j); cur = cur[:len(cur)-1] }
        }
    }
    bt(0); return res
}
func main(){ fmt.Println(partition("aab")) }
