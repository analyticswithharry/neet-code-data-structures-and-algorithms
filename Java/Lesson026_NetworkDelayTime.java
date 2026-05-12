// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 026 -- Network Delay Time
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   You are given a network of n nodes labeled from 1 to n. times[i] =
//   [u,v,w] means a signal takes w time from u to v. Starting from node k,
//   return the time it takes for all nodes to receive the signal. If
//   impossible, return -1.
//
//   Example:
//     Input : times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
//     Output: 2
// =============================================================

import java.util.*;
public class Lesson026_NetworkDelayTime {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> g = new HashMap<>();
        for (int[] t : times) g.computeIfAbsent(t[0], x -> new ArrayList<>()).add(new int[]{t[1], t[2]});
        int[] dist = new int[n+1]; Arrays.fill(dist, Integer.MAX_VALUE); dist[k] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);
        pq.offer(new int[]{0, k});
        while (!pq.isEmpty()) {
            int[] x = pq.poll(); int d = x[0], u = x[1];
            if (d > dist[u]) continue;
            for (int[] e : g.getOrDefault(u, Collections.emptyList())) {
                int nd = d + e[1];
                if (nd < dist[e[0]]) { dist[e[0]] = nd; pq.offer(new int[]{nd, e[0]}); }
            }
        }
        int mx = 0;
        for (int i = 1; i <= n; i++) { if (dist[i] == Integer.MAX_VALUE) return -1; mx = Math.max(mx, dist[i]); }
        return mx;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson026_NetworkDelayTime().networkDelayTime(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2));
    }
}
