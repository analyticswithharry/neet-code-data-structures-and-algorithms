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

import java.util.*;
public class Lesson022_ValidParentheses {
    public boolean isValid(String s) {
        Map<Character, Character> m = Map.of(')','(', ']','[', '}','{');
        Deque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (m.containsKey(c)) { if (st.isEmpty() || st.pop() != m.get(c)) return false; }
            else st.push(c);
        }
        return st.isEmpty();
    }
    public static void main(String[] args) {
        Lesson022_ValidParentheses s = new Lesson022_ValidParentheses();
        System.out.println(s.isValid("()[]{}") + " " + s.isValid("(]"));
    }
}
