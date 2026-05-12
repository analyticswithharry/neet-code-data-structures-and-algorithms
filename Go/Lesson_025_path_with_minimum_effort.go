//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 025 -- Path with Minimum Effort
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   Given an m x n grid of heights, find a path from top-left to
//   bottom-right that minimizes the maximum absolute difference in heights
//   between consecutive cells along the path.
//
//   Example:
//     Input : heights = [[1,2,2],[3,8,2],[5,3,5]]
//     Output: 2
// =============================================================

package main
import ("container/heap"; "fmt")
type Item struct { d, r, c int }
type PQ []Item
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].d < p[j].d }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(Item)) }
func (p *PQ) Pop() interface{} { o := *p; n := len(o); x := o[n-1]; *p = o[:n-1]; return x }
func abs(x int) int { if x < 0 { return -x }; return x }
func max(a,b int) int { if a > b { return a }; return b }
func minimumEffortPath(h [][]int) int {
    R, C := len(h), len(h[0])
    dist := make([][]int, R); for i := range dist { dist[i] = make([]int, C); for j := range dist[i] { dist[i][j] = 1<<30 } }
    dist[0][0] = 0
    pq := &PQ{{0,0,0}}; heap.Init(pq)
    D := [4][2]int{{1,0},{-1,0},{0,1},{0,-1}}
    for pq.Len() > 0 {
        x := heap.Pop(pq).(Item)
        if x.r == R-1 && x.c == C-1 { return x.d }
        if x.d > dist[x.r][x.c] { continue }
        for _, d := range D {
            nr, nc := x.r+d[0], x.c+d[1]
            if nr>=0 && nr<R && nc>=0 && nc<C {
                nd := max(x.d, abs(h[nr][nc]-h[x.r][x.c]))
                if nd < dist[nr][nc] { dist[nr][nc] = nd; heap.Push(pq, Item{nd,nr,nc}) }
            }
        }
    }
    return 0
}
func main() { fmt.Println(minimumEffortPath([][]int{{1,2,2},{3,8,2},{5,3,5}})) }
