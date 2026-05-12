// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 019 -- Kth Largest Element In a Stream
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Design a class to find the kth largest element in a stream. Implement:
//     KthLargest(int k, int[] nums)
//     add(val) -> returns the element representing the kth largest in the stream.
//
//   Example:
//     k=3, nums=[4,5,8,2]
//     add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
// =============================================================

import java.util.*;
public class Lesson019_KthLargestElementInAStream {
    static class KthLargest {
        PriorityQueue<Integer> pq; int k;
        public KthLargest(int k, int[] nums) {
            this.k = k; pq = new PriorityQueue<>();
            for (int n : nums) add(n);
        }
        public int add(int val) {
            if (pq.size() < k) pq.offer(val);
            else if (val > pq.peek()) { pq.poll(); pq.offer(val); }
            return pq.peek();
        }
    }
    public static void main(String[] args) {
        KthLargest kl = new KthLargest(3, new int[]{4,5,8,2});
        for (int x : new int[]{3,5,10,9,4}) System.out.print(kl.add(x) + " ");
        System.out.println();
    }
}
