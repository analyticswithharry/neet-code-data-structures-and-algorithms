// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 166 -- Jump Game II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 83
// =============================================================
//
// QUESTION:
//   Return the minimum number of jumps to reach the last index. Assume reachable.
// =============================================================
public class Lesson166_JumpGameIi{
  static int jump(int[] a){int j=0,cur=0,far=0;for(int i=0;i<a.length-1;i++){far=Math.max(far,i+a[i]);if(i==cur){j++;cur=far;}}return j;}
  public static void main(String[]x){System.out.println(jump(new int[]{2,3,1,1,4}));System.out.println(jump(new int[]{2,3,0,1,4}));}
}
