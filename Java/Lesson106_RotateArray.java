// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 106 -- Rotate Array
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Rotate the array to the right by k steps in-place.
// =============================================================

import java.util.*;
public class Lesson106_RotateArray {
    public void rotate(int[] nums, int k){
        int n=nums.length; k%=n;
        rev(nums, 0, n-1); rev(nums, 0, k-1); rev(nums, k, n-1);
    }
    void rev(int[] a, int l, int r){ while (l<r){ int t=a[l]; a[l]=a[r]; a[r]=t; l++; r--; } }
    public static void main(String[] a){
        int[] x={1,2,3,4,5,6,7}; new Lesson106_RotateArray().rotate(x, 3); System.out.println(Arrays.toString(x));
    }
}
