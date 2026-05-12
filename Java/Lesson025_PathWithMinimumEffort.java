// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 025 -- Path with Minimum Effort
// Category   : Advanced Graphs
// Difficulty : Medium
// Study Plan : Day 13
// =============================================================
//
// QUESTION:
//   Given an m x n grid of heights, find a path from top-left to
//   bottom-right that minimizes the maximum absolute difference in heights
//   between consecutive cells along the path.
//
//   Example:
//     Input : heights = [[1,2,2],[3,8,2],[5,3,5]]
//     Output: 2
// =============================================================

import java.util.*;
public class Lesson025_PathWithMinimumEffort {
    public int minimumEffortPath(int[][] h) {
        int R = h.length, C = h[0].length;
        int[][] dist = new int[R][C];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);
        pq.offer(new int[]{0,0,0});
        int[][] D = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()) {
            int[] x = pq.poll(); int d = x[0], r = x[1], c = x[2];
            if (r==R-1 && c==C-1) return d;
            if (d > dist[r][c]) continue;
            for (int[] dd : D) {
                int nr=r+dd[0], nc=c+dd[1];
                if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                    int nd = Math.max(d, Math.abs(h[nr][nc]-h[r][c]));
                    if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.offer(new int[]{nd,nr,nc}); }
                }
            }
        }
        return 0;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson025_PathWithMinimumEffort().minimumEffortPath(new int[][]{{1,2,2},{3,8,2},{5,3,5}}));
    }
}
