//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 091 -- Single Threaded CPU
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
// =============================================================

package main
import ( "container/heap"; "fmt"; "sort" )
type T struct{ p,i int }
type H []T
func (h H) Len()int{return len(h)}
func (h H) Less(i,j int)bool{ if h[i].p!=h[j].p{return h[i].p<h[j].p}; return h[i].i<h[j].i }
func (h H) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *H) Push(x any){*h=append(*h,x.(T))}
func (h *H) Pop()any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func getOrder(tasks [][]int) []int {
    n:=len(tasks); idx:=make([]int,n); for i:=range idx{idx[i]=i}
    sort.Slice(idx, func(a,b int)bool{return tasks[idx[a]][0]<tasks[idx[b]][0]})
    h:=&H{}; heap.Init(h); var t int64=0; i:=0; res:=[]int{}
    for i<n || h.Len()>0 {
        if h.Len()==0 { if int64(tasks[idx[i]][0])>t { t=int64(tasks[idx[i]][0]) } }
        for i<n && int64(tasks[idx[i]][0])<=t { heap.Push(h, T{tasks[idx[i]][1], idx[i]}); i++ }
        x:=heap.Pop(h).(T); t+=int64(x.p); res=append(res,x.i)
    }
    return res
}
func main(){ fmt.Println(getOrder([][]int{{1,2},{2,4},{3,2},{4,1}})) }
