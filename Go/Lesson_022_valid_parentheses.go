//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 022 -- Valid Parentheses
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   Given a string s containing just the characters '(', ')', '{', '}',
//   '[' and ']', determine if the input string is valid. An input string is
//   valid if open brackets are closed by the same type of brackets in the
//   correct order.
//
//   Example:
//     Input : "()[]{}"   Output: true
//     Input : "(]"       Output: false
// =============================================================

package main
import "fmt"
func isValid(s string) bool {
    m := map[byte]byte{')':'(', ']':'[', '}':'{'}
    st := []byte{}
    for i := 0; i < len(s); i++ {
        c := s[i]
        if op, ok := m[c]; ok {
            if len(st) == 0 || st[len(st)-1] != op { return false }
            st = st[:len(st)-1]
        } else { st = append(st, c) }
    }
    return len(st) == 0
}
func main() { fmt.Println(isValid("()[]{}"), isValid("(]")) }
