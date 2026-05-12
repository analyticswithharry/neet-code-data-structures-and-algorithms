//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 059 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Design a time-based key-value data structure that supports
//   set(key, value, timestamp) and get(key, timestamp), where get returns
//   the value with the largest timestamp <= the given timestamp.
// =============================================================

package main
import "fmt"
type entry struct{ t int; v string }
type TimeMap struct{ d map[string][]entry }
func New() *TimeMap { return &TimeMap{d: map[string][]entry{}} }
func (m *TimeMap) Set(k, v string, t int) { m.d[k] = append(m.d[k], entry{t, v}) }
func (m *TimeMap) Get(k string, t int) string {
    a, ok := m.d[k]; if !ok { return "" }
    l, r, res := 0, len(a)-1, ""
    for l <= r {
        mid := (l+r)/2
        if a[mid].t <= t { res = a[mid].v; l = mid+1 } else { r = mid-1 }
    }
    return res
}
func main(){
    tm := New(); tm.Set("foo","bar",1)
    fmt.Println(tm.Get("foo",1), tm.Get("foo",3))
    tm.Set("foo","bar2",4)
    fmt.Println(tm.Get("foo",4), tm.Get("foo",5))
}
