// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 038 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
//
//   Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
// =============================================================

import java.util.*;
public class Lesson038_TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> c = new HashMap<>();
        for (int n: nums) c.merge(n, 1, Integer::sum);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->b[1]-a[1]);
        for (var e: c.entrySet()) pq.add(new int[]{e.getKey(), e.getValue()});
        int[] r = new int[k];
        for (int i=0;i<k;i++) r[i] = pq.poll()[0];
        return r;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new Lesson038_TopKFrequentElements().topKFrequent(new int[]{1,1,1,2,2,3}, 2)));
    }
}
