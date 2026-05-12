// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 053 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Cars at given positions move toward target with given speeds. A car
//   that catches up forms a fleet. Return the number of fleets that arrive.
//
//   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
// =============================================================

import java.util.*;
public class Lesson053_CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] idx = new Integer[n];
        for (int i=0;i<n;i++) idx[i] = i;
        Arrays.sort(idx, (a,b) -> position[b] - position[a]);
        Deque<Double> st = new ArrayDeque<>();
        for (int i: idx) {
            double t = (double)(target - position[i]) / speed[i];
            if (st.isEmpty() || t > st.peek()) st.push(t);
        }
        return st.size();
    }
    public static void main(String[] a){
        System.out.println(new Lesson053_CarFleet().carFleet(12, new int[]{10,8,0,5,3}, new int[]{2,4,1,1,3}));
    }
}
