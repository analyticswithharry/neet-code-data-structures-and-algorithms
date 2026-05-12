// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 040 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Given an unsorted array, return the length of the longest consecutive
//   elements sequence in O(n).
//
//   Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)
// =============================================================

import java.util.*;
public class Lesson040_LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int n: nums) s.add(n);
        int best = 0;
        for (int n: s) if (!s.contains(n-1)) {
            int cur = n, len = 1;
            while (s.contains(cur+1)) { cur++; len++; }
            best = Math.max(best, len);
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new Lesson040_LongestConsecutiveSequence().longestConsecutive(new int[]{100,4,200,1,3,2}));
    }
}
