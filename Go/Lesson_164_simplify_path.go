//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 164 -- Simplify Path
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Given a Unix-style absolute path, return the simplified canonical path.
// =============================================================
package main
import ("fmt"; "strings")
func simplify(p string) string { st:=[]string{}; for _,part:=range strings.Split(p,"/") { if part==""||part=="." { continue }; if part==".." { if len(st)>0 { st=st[:len(st)-1] } } else { st=append(st,part) } }; return "/"+strings.Join(st,"/") }
func main(){ fmt.Println(simplify("/a/./b/../../c/")); fmt.Println(simplify("/home//foo/")) }
