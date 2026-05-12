// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 039 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 19
// =============================================================
//
// QUESTION:
//   Given nums, return an array where answer[i] is the product of all elements
//   except nums[i]. Must run in O(n) without division.
//
//   Example: [1,2,3,4] -> [24,12,8,6]
// =============================================================

import java.util.*;
public class Lesson039_ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length; int[] r = new int[n];
        int left = 1;
        for (int i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
        int right = 1;
        for (int i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
        return r;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new Lesson039_ProductOfArrayExceptSelf().productExceptSelf(new int[]{1,2,3,4})));
    }
}
