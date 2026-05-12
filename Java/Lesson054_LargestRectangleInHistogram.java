// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 054 -- Largest Rectangle in Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given heights of bars, find the area of the largest rectangle.
//
//   Example: [2,1,5,6,2,3] -> 10
// =============================================================

import java.util.*;
public class Lesson054_LargestRectangleInHistogram {
    public int largestRectangleArea(int[] h) {
        Deque<int[]> st = new ArrayDeque<>(); int best = 0;
        int n = h.length;
        for (int i=0;i<=n;i++) {
            int v = (i==n) ? 0 : h[i];
            int start = i;
            while (!st.isEmpty() && st.peek()[1] > v) {
                int[] top = st.pop();
                best = Math.max(best, top[1] * (i - top[0]));
                start = top[0];
            }
            st.push(new int[]{start, v});
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new Lesson054_LargestRectangleInHistogram().largestRectangleArea(new int[]{2,1,5,6,2,3}));
    }
}
