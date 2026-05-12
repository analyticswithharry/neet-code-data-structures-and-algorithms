// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 035 -- Sum of All Subsets XOR Total
// Category   : Backtracking
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   The XOR total of an array is the bitwise XOR of all its elements (or 0
//   if empty). Return the sum of all XOR totals for every subset of nums.
//
//   Example:
//     Input : [1,3]      Output: 6   (subsets: [],[1],[3],[1,3] -> 0+1+3+2 = 6)
//     Input : [5,1,6]    Output: 28
// =============================================================

public class Lesson035_SumOfAllSubsetsXorTotal {
    int total = 0;
    public int subsetXORSum(int[] nums) { total = 0; dfs(nums, 0, 0); return total; }
    void dfs(int[] nums, int i, int cur) {
        if (i == nums.length) { total += cur; return; }
        dfs(nums, i+1, cur); dfs(nums, i+1, cur ^ nums[i]);
    }
    public static void main(String[] args) {
        Lesson035_SumOfAllSubsetsXorTotal s = new Lesson035_SumOfAllSubsetsXorTotal();
        System.out.println(s.subsetXORSum(new int[]{1,3}) + " " + s.subsetXORSum(new int[]{5,1,6}));
    }
}
