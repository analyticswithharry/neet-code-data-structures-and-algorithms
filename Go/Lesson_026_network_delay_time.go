//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 026 -- Network Delay Time
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   You are given a network of n nodes labeled from 1 to n. times[i] =
//   [u,v,w] means a signal takes w time from u to v. Starting from node k,
//   return the time it takes for all nodes to receive the signal. If
//   impossible, return -1.
//
//   Example:
//     Input : times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
//     Output: 2
// =============================================================

package main
import ("container/heap"; "fmt")
type E struct { d, u int }
type PQ []E
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].d < p[j].d }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(E)) }
func (p *PQ) Pop() interface{} { o := *p; n := len(o); x := o[n-1]; *p = o[:n-1]; return x }
func networkDelayTime(times [][]int, n, k int) int {
    g := make(map[int][][2]int)
    for _, t := range times { g[t[0]] = append(g[t[0]], [2]int{t[1], t[2]}) }
    const INF = 1 << 30
    dist := make([]int, n+1); for i := range dist { dist[i] = INF }
    dist[k] = 0
    pq := &PQ{{0, k}}; heap.Init(pq)
    for pq.Len() > 0 {
        x := heap.Pop(pq).(E)
        if x.d > dist[x.u] { continue }
        for _, e := range g[x.u] {
            nd := x.d + e[1]
            if nd < dist[e[0]] { dist[e[0]] = nd; heap.Push(pq, E{nd, e[0]}) }
        }
    }
    mx := 0
    for i := 1; i <= n; i++ { if dist[i] == INF { return -1 }; if dist[i] > mx { mx = dist[i] } }
    return mx
}
func main() { fmt.Println(networkDelayTime([][]int{{2,1,1},{2,3,1},{3,4,1}}, 4, 2)) }
