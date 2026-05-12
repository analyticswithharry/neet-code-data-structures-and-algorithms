//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 089 -- Reconstruct Itinerary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
// =============================================================

package main
import ( "fmt"; "sort" )
func findItinerary(tickets [][]string) []string {
    g := map[string][]string{}
    for _, t := range tickets { g[t[0]] = append(g[t[0]], t[1]) }
    for k := range g { sort.Sort(sort.Reverse(sort.StringSlice(g[k]))) }
    st := []string{"JFK"}; res := []string{}
    for len(st) > 0 {
        top := st[len(st)-1]
        for len(g[top]) > 0 {
            n := len(g[top]); nxt := g[top][n-1]; g[top] = g[top][:n-1]
            st = append(st, nxt); top = nxt
        }
        res = append(res, st[len(st)-1]); st = st[:len(st)-1]
    }
    for i,j:=0,len(res)-1; i<j; i,j=i+1,j-1 { res[i],res[j]=res[j],res[i] }
    return res
}
func main(){ fmt.Println(findItinerary([][]string{{"MUC","LHR"},{"JFK","MUC"},{"SFO","SJC"},{"LHR","SFO"}})) }
