// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 168 -- Maximum Product Subarray
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 84
// =============================================================
//
// QUESTION:
//   Find a contiguous subarray with the largest product.
// =============================================================
public class Lesson168_MaximumProductSubarray{
  static int maxProduct(int[] a){int mx=a[0],mn=a[0],res=a[0];for(int i=1;i<a.length;i++){int v=a[i];if(v<0){int t=mx;mx=mn;mn=t;}mx=Math.max(v,mx*v);mn=Math.min(v,mn*v);res=Math.max(res,mx);}return res;}
  public static void main(String[]x){System.out.println(maxProduct(new int[]{2,3,-2,4}));System.out.println(maxProduct(new int[]{-2,0,-1}));}
}
