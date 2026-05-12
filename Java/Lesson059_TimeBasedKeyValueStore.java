// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 059 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Design a time-based key-value data structure that supports
//   set(key, value, timestamp) and get(key, timestamp), where get returns
//   the value with the largest timestamp <= the given timestamp.
// =============================================================

import java.util.*;
public class Lesson059_TimeBasedKeyValueStore {
    static class TimeMap {
        Map<String, List<int[]>> ts = new HashMap<>();
        Map<String, List<String>> vs = new HashMap<>();
        public void set(String k, String v, int t){
            ts.computeIfAbsent(k, x -> new ArrayList<>()).add(new int[]{t});
            vs.computeIfAbsent(k, x -> new ArrayList<>()).add(v);
        }
        public String get(String k, int t){
            if (!ts.containsKey(k)) return "";
            List<int[]> a = ts.get(k); List<String> b = vs.get(k);
            int l = 0, r = a.size()-1; String res = "";
            while (l <= r) {
                int m = (l+r)/2;
                if (a.get(m)[0] <= t) { res = b.get(m); l = m+1; } else r = m-1;
            }
            return res;
        }
    }
    public static void main(String[] a){
        TimeMap tm = new TimeMap(); tm.set("foo","bar",1);
        System.out.println(tm.get("foo",1)); System.out.println(tm.get("foo",3));
        tm.set("foo","bar2",4);
        System.out.println(tm.get("foo",4)); System.out.println(tm.get("foo",5));
    }
}
