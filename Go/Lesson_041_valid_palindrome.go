//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 041 -- Valid Palindrome
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Return true if s is a palindrome considering only alphanumeric chars
//   and ignoring case.
//
//   Example: "A man, a plan, a canal: Panama" -> true
// =============================================================

package main
import ("fmt"; "unicode")
func isPalindrome(s string) bool {
    r := []rune(s); i, j := 0, len(r)-1
    for i < j {
        for i<j && !unicode.IsLetter(r[i]) && !unicode.IsDigit(r[i]) { i++ }
        for i<j && !unicode.IsLetter(r[j]) && !unicode.IsDigit(r[j]) { j-- }
        if unicode.ToLower(r[i]) != unicode.ToLower(r[j]) { return false }
        i++; j--
    }
    return true
}
func main(){ fmt.Println(isPalindrome("A man, a plan, a canal: Panama"), isPalindrome("race a car")) }
