//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 050 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 25
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation.
//
//   Example: ["2","1","+","3","*"] -> 9
// =============================================================

package main
import ("fmt"; "strconv")
func evalRPN(tokens []string) int {
    st := []int{}
    for _,t := range tokens {
        switch t {
        case "+","-","*","/":
            b := st[len(st)-1]; a := st[len(st)-2]; st = st[:len(st)-2]
            switch t {
            case "+": st = append(st, a+b)
            case "-": st = append(st, a-b)
            case "*": st = append(st, a*b)
            case "/": st = append(st, a/b)
            }
        default:
            n, _ := strconv.Atoi(t); st = append(st, n)
        }
    }
    return st[0]
}
func main(){ fmt.Println(evalRPN([]string{"2","1","+","3","*"})) }
