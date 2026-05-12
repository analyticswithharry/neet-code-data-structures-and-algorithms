// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 098 -- Sort Colors
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Sort an array containing only 0, 1, 2 in-place (Dutch national flag).
// =============================================================

import java.util.*;
public class Lesson098_SortColors {
    public void sortColors(int[] nums){
        int l=0, m=0, r=nums.length-1;
        while (m<=r){
            if (nums[m]==0){ int t=nums[l]; nums[l]=nums[m]; nums[m]=t; l++; m++; }
            else if (nums[m]==2){ int t=nums[r]; nums[r]=nums[m]; nums[m]=t; r--; }
            else m++;
        }
    }
    public static void main(String[] a){
        int[] x={2,0,2,1,1,0}; new Lesson098_SortColors().sortColors(x); System.out.println(Arrays.toString(x));
    }
}
