// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 034 -- Kth Largest Element In An Array
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 17
// =============================================================
//
// QUESTION:
//   Given an integer array nums and an integer k, return the kth largest
//   element in the array (the kth largest in sorted order, not the kth
//   distinct element).
//
//   Example:
//     Input : [3,2,1,5,6,4], k=2   Output: 5
// =============================================================

import java.util.*;
public class Lesson034_KthLargestElementInAnArray {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n : nums) { pq.offer(n); if (pq.size() > k) pq.poll(); }
        return pq.peek();
    }
    public static void main(String[] args) {
        System.out.println(new Lesson034_KthLargestElementInAnArray().findKthLargest(new int[]{3,2,1,5,6,4}, 2));
    }
}
