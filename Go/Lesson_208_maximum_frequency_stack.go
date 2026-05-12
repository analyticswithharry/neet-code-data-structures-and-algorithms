//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 208 -- Maximum Frequency Stack
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Push/pop a stack returning the most-frequent element (ties: most recent).
// =============================================================
package main
import "fmt"
type FreqStack struct { f map[int]int; g map[int][]int; maxf int }
func New() *FreqStack { return &FreqStack{f:map[int]int{},g:map[int][]int{}} }
func (s *FreqStack) Push(v int) { s.f[v]++; if s.f[v]>s.maxf { s.maxf=s.f[v] }; s.g[s.f[v]]=append(s.g[s.f[v]],v) }
func (s *FreqStack) Pop() int { arr:=s.g[s.maxf]; v:=arr[len(arr)-1]; s.g[s.maxf]=arr[:len(arr)-1]; s.f[v]--; if len(s.g[s.maxf])==0 { s.maxf-- }; return v }
func main(){ fs:=New(); for _,x:=range []int{5,7,5,7,4,5} { fs.Push(x) }; for i:=0;i<4;i++ { fmt.Print(fs.Pop()," ") }; fmt.Println() }
