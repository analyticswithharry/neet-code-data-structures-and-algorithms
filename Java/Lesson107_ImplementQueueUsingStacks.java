// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 107 -- Implement Queue using Stacks
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Implement a FIFO queue using only two stacks.
// =============================================================

import java.util.*;
public class Lesson107_ImplementQueueUsingStacks {
    Deque<Integer> a = new ArrayDeque<>(), b = new ArrayDeque<>();
    public void push(int x){ a.push(x); }
    public int pop(){ peek(); return b.pop(); }
    public int peek(){ if (b.isEmpty()) while (!a.isEmpty()) b.push(a.pop()); return b.peek(); }
    public boolean empty(){ return a.isEmpty() && b.isEmpty(); }
    public static void main(String[] a){
        Lesson107_ImplementQueueUsingStacks q = new Lesson107_ImplementQueueUsingStacks(); q.push(1); q.push(2);
        System.out.println(q.peek()); System.out.println(q.pop()); System.out.println(q.empty());
    }
}
