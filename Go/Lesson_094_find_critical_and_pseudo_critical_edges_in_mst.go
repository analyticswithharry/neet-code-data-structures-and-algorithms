//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
// =============================================================

package main
import ( "fmt"; "sort" )
type DSU struct{ p, r []int; cnt int }
func NewDSU(n int) *DSU { d:=&DSU{p:make([]int,n), r:make([]int,n), cnt:n}; for i:=range d.p{d.p[i]=i}; return d }
func (d *DSU) f(x int) int { for d.p[x]!=x { d.p[x]=d.p[d.p[x]]; x=d.p[x] }; return x }
func (d *DSU) u(a,b int) bool { a,b=d.f(a),d.f(b); if a==b{return false}
    if d.r[a]<d.r[b]{a,b=b,a}; d.p[b]=a; if d.r[a]==d.r[b]{d.r[a]++}; d.cnt--; return true }
func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
    E := make([][]int, len(edges))
    for i, e := range edges { E[i] = []int{e[0], e[1], e[2], i} }
    sort.Slice(E, func(i,j int) bool { return E[i][2] < E[j][2] })
    kruskal := func(skip, force int) int {
        d := NewDSU(n); w := 0
        if force >= 0 { if !d.u(E[force][0], E[force][1]) { return 1<<30 }; w += E[force][2] }
        for i, e := range E { if i==skip { continue }; if d.u(e[0], e[1]) { w += e[2] } }
        if d.cnt != 1 { return 1<<30 }; return w
    }
    base := kruskal(-1,-1)
    crit, pseu := []int{}, []int{}
    for i, e := range E {
        if kruskal(i,-1) > base { crit = append(crit, e[3]) } else if kruskal(-1,i) == base { pseu = append(pseu, e[3]) }
    }
    return [][]int{crit, pseu}
}
func main(){ fmt.Println(findCriticalAndPseudoCriticalEdges(5, [][]int{{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}})) }
