// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 103 -- Merge Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.
// =============================================================

import java.util.*;
public class Lesson103_MergeIntervals {
    public int[][] merge(int[][] intervals){
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        List<int[]> res = new ArrayList<>();
        for (int[] x: intervals){
            if (!res.isEmpty() && x[0] <= res.get(res.size()-1)[1])
                res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], x[1]);
            else res.add(new int[]{x[0], x[1]});
        }
        return res.toArray(new int[0][]);
    }
    public static void main(String[] a){
        int[][] r = new Lesson103_MergeIntervals().merge(new int[][]{{1,3},{2,6},{8,10},{15,18}});
        System.out.println(Arrays.deepToString(r));
    }
}
