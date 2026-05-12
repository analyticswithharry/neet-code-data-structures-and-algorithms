//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 163 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
// =============================================================
package main
import ("fmt"; "sort")
func carFleet(target int,pos,sp []int) int { n:=len(pos); idx:=make([]int,n); for i:=range idx { idx[i]=i }; sort.Slice(idx,func(i,j int) bool { return pos[idx[i]]>pos[idx[j]] }); f:=0; lt:=0.0; for _,i:=range idx { t:=float64(target-pos[i])/float64(sp[i]); if t>lt { f++; lt=t } }; return f }
func main(){ fmt.Println(carFleet(12,[]int{10,8,0,5,3},[]int{2,4,1,1,3})) }
