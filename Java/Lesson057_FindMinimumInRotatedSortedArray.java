// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 057 -- Find Minimum in Rotated Sorted Array
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 28
// =============================================================
//
// QUESTION:
//   Given a rotated sorted array of unique elements, return its minimum.
//
//   Example: [3,4,5,1,2] -> 1
// =============================================================

public class Lesson057_FindMinimumInRotatedSortedArray {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l+r)/2;
            if (nums[mid] > nums[r]) l = mid+1; else r = mid;
        }
        return nums[l];
    }
    public static void main(String[] a){
        Lesson057_FindMinimumInRotatedSortedArray s = new Lesson057_FindMinimumInRotatedSortedArray();
        System.out.println(s.findMin(new int[]{3,4,5,1,2}));
        System.out.println(s.findMin(new int[]{4,5,6,7,0,1,2}));
    }
}
