// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 052 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Given temperatures, for each day return the number of days until a
//   warmer temperature, or 0 if none.
//
//   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
// =============================================================

import java.util.*;
public class Lesson052_DailyTemperatures {
    public int[] dailyTemperatures(int[] t) {
        int n = t.length; int[] res = new int[n];
        Deque<Integer> st = new ArrayDeque<>();
        for (int i=0;i<n;i++) {
            while (!st.isEmpty() && t[st.peek()] < t[i]) {
                int j = st.pop(); res[j] = i - j;
            }
            st.push(i);
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new Lesson052_DailyTemperatures().dailyTemperatures(new int[]{73,74,75,71,69,72,76,73})));
    }
}
