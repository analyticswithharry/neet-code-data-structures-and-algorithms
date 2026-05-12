// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 060 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 30
// =============================================================
//
// QUESTION:
//   Given two sorted arrays nums1 and nums2, return the median of the
//   combined sorted array. Run in O(log(min(m,n))).
//
//   Example: [1,3], [2] -> 2.0
// =============================================================

public class Lesson060_MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] a, int[] b) {
        if (a.length > b.length) { int[] t = a; a = b; b = t; }
        int m = a.length, n = b.length, half = (m+n+1)/2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo+hi)/2, j = half - i;
            int la = i>0 ? a[i-1] : Integer.MIN_VALUE;
            int ra = i<m ? a[i]   : Integer.MAX_VALUE;
            int lb = j>0 ? b[j-1] : Integer.MIN_VALUE;
            int rb = j<n ? b[j]   : Integer.MAX_VALUE;
            if (la <= rb && lb <= ra) {
                if ((m+n) % 2 == 1) return Math.max(la, lb);
                return (Math.max(la, lb) + Math.min(ra, rb)) / 2.0;
            } else if (la > rb) hi = i-1;
            else lo = i+1;
        }
        return 0.0;
    }
    public static void main(String[] a){
        Lesson060_MedianOfTwoSortedArrays s = new Lesson060_MedianOfTwoSortedArrays();
        System.out.println(s.findMedianSortedArrays(new int[]{1,3}, new int[]{2}));
        System.out.println(s.findMedianSortedArrays(new int[]{1,2}, new int[]{3,4}));
    }
}
