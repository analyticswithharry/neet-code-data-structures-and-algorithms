//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 090 -- Swim In Rising Water
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
// =============================================================

package main
import ( "container/heap"; "fmt" )
type Item struct{ v,r,c int }
type PQ []Item
func (p PQ) Len()int{return len(p)}
func (p PQ) Less(i,j int)bool{return p[i].v<p[j].v}
func (p PQ) Swap(i,j int){p[i],p[j]=p[j],p[i]}
func (p *PQ) Push(x any){*p=append(*p,x.(Item))}
func (p *PQ) Pop()any{o:=*p; n:=len(o); x:=o[n-1]; *p=o[:n-1]; return x}
func swimInWater(g [][]int) int {
    n:=len(g); pq:=&PQ{}; heap.Init(pq); heap.Push(pq, Item{g[0][0],0,0})
    seen:=make([][]bool,n); for i:=range seen{seen[i]=make([]bool,n)}; seen[0][0]=true; ans:=0
    dr:=[]int{1,-1,0,0}; dc:=[]int{0,0,1,-1}
    for pq.Len()>0 {
        x:=heap.Pop(pq).(Item); if x.v>ans{ans=x.v}
        if x.r==n-1 && x.c==n-1 { return ans }
        for k:=0;k<4;k++{ nr,nc:=x.r+dr[k],x.c+dc[k]
            if nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]{ seen[nr][nc]=true; heap.Push(pq, Item{g[nr][nc],nr,nc}) }
        }
    }
    return -1
}
func main(){ fmt.Println(swimInWater([][]int{{0,2},{1,3}})) }
