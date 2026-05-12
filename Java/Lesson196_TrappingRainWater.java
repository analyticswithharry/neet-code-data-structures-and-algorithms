// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 196 -- Trapping Rain Water
// Category   : Two Pointers
// Difficulty : Hard
// Study Plan : Day 98
// =============================================================
//
// QUESTION:
//   Compute total water trapped between bars given heights.
// =============================================================
public class Lesson196_TrappingRainWater{
  static int trap(int[] h){int l=0,r=h.length-1,lm=0,rm=0,res=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lm)lm=h[l];else res+=lm-h[l];l++;}else{if(h[r]>=rm)rm=h[r];else res+=rm-h[r];r--;}}return res;}
  public static void main(String[]a){System.out.println(trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));}
}
