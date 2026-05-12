//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 162 -- Multiply Strings
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
// =============================================================
package main
import "fmt"
func mul(a,b string) string { if a=="0"||b=="0" { return "0" }; n,m:=len(a),len(b); r:=make([]int,n+m); for i:=n-1;i>=0;i-- { for j:=m-1;j>=0;j-- { p:=int(a[i]-'0')*int(b[j]-'0'); s:=p+r[i+j+1]; r[i+j+1]=s%10; r[i+j]+=s/10 } }; out:=""; for _,v:=range r { out+=string(rune('0'+v)) }; for len(out)>1 && out[0]=='0' { out=out[1:] }; return out }
func main(){ fmt.Println(mul("123","456")) }
