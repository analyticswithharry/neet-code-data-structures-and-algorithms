//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 108 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.
// =============================================================

package main
import ( "fmt"; "strconv" )
func evalRPN(tokens []string) int {
    st := []int{}
    for _, t := range tokens {
        if len(t)==1 && (t=="+"||t=="-"||t=="*"||t=="/") {
            n := len(st); b, a := st[n-1], st[n-2]; st = st[:n-2]
            switch t { case "+": st = append(st, a+b); case "-": st = append(st, a-b); case "*": st = append(st, a*b); case "/": st = append(st, a/b) }
        } else { v, _ := strconv.Atoi(t); st = append(st, v) }
    }
    return st[0]
}
func main(){ fmt.Println(evalRPN([]string{"2","1","+","3","*"}), evalRPN([]string{"10","6","9","3","+","-11","*","/","*","17","+","5","+"})) }
