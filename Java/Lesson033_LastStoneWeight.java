// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 033 -- Last Stone Weight
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   You are given an array of stones. On each turn pick the two heaviest
//   stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
//   and y becomes y - x. Return the weight of the last remaining stone (or 0).
//
//   Example:
//     Input : [2,7,4,1,8,1]   Output: 1
// =============================================================

import java.util.*;
public class Lesson033_LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int s : stones) pq.offer(s);
        while (pq.size() > 1) {
            int y = pq.poll(), x = pq.poll();
            if (y != x) pq.offer(y - x);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
    public static void main(String[] args) {
        System.out.println(new Lesson033_LastStoneWeight().lastStoneWeight(new int[]{2,7,4,1,8,1}));
    }
}
