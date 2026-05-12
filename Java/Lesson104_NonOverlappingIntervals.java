// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 104 -- Non Overlapping Intervals
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 52
// =============================================================
//
// QUESTION:
//   Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.
// =============================================================

import java.util.*;
public class Lesson104_NonOverlappingIntervals {
    public int eraseOverlapIntervals(int[][] intervals){
        Arrays.sort(intervals, (a,b)->a[1]-b[1]);
        int end = Integer.MIN_VALUE, rm = 0;
        for (int[] x: intervals){ if (x[0]>=end) end=x[1]; else rm++; }
        return rm;
    }
    public static void main(String[] a){
        System.out.println(new Lesson104_NonOverlappingIntervals().eraseOverlapIntervals(new int[][]{{1,2},{2,3},{3,4},{1,3}}));
    }
}
