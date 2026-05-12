// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 042 -- 3Sum
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
//
//   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
// =============================================================

import java.util.*;
public class Lesson042_3sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); List<List<Integer>> res = new ArrayList<>();
        for (int i=0;i<nums.length-2;i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            int l=i+1, r=nums.length-1;
            while (l<r) {
                int s = nums[i]+nums[l]+nums[r];
                if (s<0) l++;
                else if (s>0) r--;
                else {
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    while (l<r && nums[l]==nums[l+1]) l++;
                    while (l<r && nums[r]==nums[r-1]) r--;
                    l++; r--;
                }
            }
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(new Lesson042_3sum().threeSum(new int[]{-1,0,1,2,-1,-4}));
    }
}
