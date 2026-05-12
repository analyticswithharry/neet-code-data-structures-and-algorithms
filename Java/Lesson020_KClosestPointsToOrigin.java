// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 020 -- K Closest Points to Origin
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Given an array of points where points[i] = [xi, yi] and an integer k,
//   return the k closest points to the origin (0, 0). Distance is Euclidean.
//
//   Example:
//     Input : points = [[1,3],[-2,2]], k = 1
//     Output: [[-2,2]]
// =============================================================

import java.util.*;
public class Lesson020_KClosestPointsToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) ->
            (b[0]*b[0]+b[1]*b[1]) - (a[0]*a[0]+a[1]*a[1]));
        for (int[] p : points) { pq.offer(p); if (pq.size() > k) pq.poll(); }
        int[][] out = new int[k][];
        for (int i = 0; i < k; i++) out[i] = pq.poll();
        return out;
    }
    public static void main(String[] args) {
        int[][] r = new Lesson020_KClosestPointsToOrigin().kClosest(new int[][]{{3,3},{5,-1},{-2,4}}, 2);
        for (int[] p : r) System.out.println(p[0] + "," + p[1]);
    }
}
