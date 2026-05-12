// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 049 -- Min Stack
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Design a stack supporting push, pop, top, and getMin in O(1).
// =============================================================

import java.util.*;
public class Lesson049_MinStack {
    static class MinStack {
        Deque<Integer> s = new ArrayDeque<>(), m = new ArrayDeque<>();
        public void push(int v){ s.push(v); m.push(m.isEmpty()?v:Math.min(v,m.peek())); }
        public void pop(){ s.pop(); m.pop(); }
        public int top(){ return s.peek(); }
        public int getMin(){ return m.peek(); }
    }
    public static void main(String[] a){
        MinStack s = new MinStack(); s.push(-2); s.push(0); s.push(-3);
        System.out.println(s.getMin()); s.pop();
        System.out.println(s.top()); System.out.println(s.getMin());
    }
}
