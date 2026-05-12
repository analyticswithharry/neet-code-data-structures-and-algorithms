// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 087 -- Subsets II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
//   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
// =============================================================

import java.util.*;
public class Lesson087_SubsetsIi {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> subsetsWithDup(int[] nums){
        Arrays.sort(nums); bt(nums,0,new ArrayList<>()); return res;
    }
    void bt(int[] nums, int i, List<Integer> cur){
        res.add(new ArrayList<>(cur));
        for (int j=i;j<nums.length;j++){
            if (j>i && nums[j]==nums[j-1]) continue;
            cur.add(nums[j]); bt(nums,j+1,cur); cur.remove(cur.size()-1);
        }
    }
    public static void main(String[] a){
        System.out.println(new Lesson087_SubsetsIi().subsetsWithDup(new int[]{1,2,2}));
    }
}
