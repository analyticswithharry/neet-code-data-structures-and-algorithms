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

import java.util.*;
public class Lesson021_BaseballGame {
    public int calPoints(String[] ops) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String o : ops) {
            switch (o) {
                case "+": { int a = st.pop(), b = st.peek(); st.push(a); st.push(a+b); break; }
                case "D": st.push(2 * st.peek()); break;
                case "C": st.pop(); break;
                default:  st.push(Integer.parseInt(o));
            }
        }
        int s = 0; for (int x : st) s += x; return s;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson021_BaseballGame().calPoints(new String[]{"5","2","C","D","+"}));
    }
}
