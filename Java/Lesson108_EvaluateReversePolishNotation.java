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

import java.util.*;
public class Lesson108_EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens){
        Deque<Integer> st = new ArrayDeque<>();
        for (String t: tokens){
            if (t.length()==1 && "+-*/".indexOf(t.charAt(0))>=0){
                int b=st.pop(), a=st.pop();
                switch (t.charAt(0)){
                    case '+': st.push(a+b); break;
                    case '-': st.push(a-b); break;
                    case '*': st.push(a*b); break;
                    default: st.push(a/b);
                }
            } else st.push(Integer.parseInt(t));
        }
        return st.peek();
    }
    public static void main(String[] a){
        System.out.println(new Lesson108_EvaluateReversePolishNotation().evalRPN(new String[]{"2","1","+","3","*"}));
        System.out.println(new Lesson108_EvaluateReversePolishNotation().evalRPN(new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
    }
}
