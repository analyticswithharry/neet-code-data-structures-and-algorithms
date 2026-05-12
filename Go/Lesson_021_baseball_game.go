//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 021 -- Baseball Game
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   You are keeping the scores for a baseball game. Operations:
//     Integer x : record a new score x
//     '+'       : record sum of previous two scores
//     'D'       : record double of previous score
//     'C'       : invalidate the previous score, removing it
//   Return the sum of all the scores after all operations.
//
//   Example:
//     Input : ops = ["5","2","C","D","+"]
//     Output: 30   (records: 5, 10, 15)
// =============================================================

package main
import ("fmt"; "strconv")
func calPoints(ops []string) int {
    st := []int{}
    for _, o := range ops {
        switch o {
        case "+": st = append(st, st[len(st)-1]+st[len(st)-2])
        case "D": st = append(st, 2*st[len(st)-1])
        case "C": st = st[:len(st)-1]
        default: n, _ := strconv.Atoi(o); st = append(st, n)
        }
    }
    s := 0; for _, v := range st { s += v }; return s
}
func main() { fmt.Println(calPoints([]string{"5","2","C","D","+"})) }
