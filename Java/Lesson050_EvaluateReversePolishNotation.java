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

import java.util.*;
public class Lesson050_EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String t: tokens) {
            if ("+-*/".contains(t) && t.length()==1) {
                int b = st.pop(), a = st.pop();
                switch (t.charAt(0)) {
                    case '+': st.push(a+b); break;
                    case '-': st.push(a-b); break;
                    case '*': st.push(a*b); break;
                    default:  st.push(a/b);
                }
            } else st.push(Integer.parseInt(t));
        }
        return st.pop();
    }
    public static void main(String[] a){
        System.out.println(new Lesson050_EvaluateReversePolishNotation().evalRPN(new String[]{"2","1","+","3","*"}));
    }
}
