// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 088 -- Permutations II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
//   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
// =============================================================

import java.util.*;
public class Lesson088_PermutationsIi {
    List<List<Integer>> res = new ArrayList<>();
    boolean[] used; int[] nums;
    public List<List<Integer>> permuteUnique(int[] n){
        Arrays.sort(n); nums=n; used=new boolean[n.length];
        bt(new ArrayList<>()); return res;
    }
    void bt(List<Integer> cur){
        if (cur.size()==nums.length){ res.add(new ArrayList<>(cur)); return; }
        for (int i=0;i<nums.length;i++){
            if (used[i]) continue;
            if (i>0 && nums[i]==nums[i-1] && !used[i-1]) continue;
            used[i]=true; cur.add(nums[i]); bt(cur); cur.remove(cur.size()-1); used[i]=false;
        }
    }
    public static void main(String[] a){ System.out.println(new Lesson088_PermutationsIi().permuteUnique(new int[]{1,1,2})); }
}
