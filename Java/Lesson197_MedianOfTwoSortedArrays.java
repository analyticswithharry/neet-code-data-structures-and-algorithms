// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 197 -- Median of Two Sorted Arrays
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 99
// =============================================================
//
// QUESTION:
//   Find the median of the two sorted arrays in O(log(min(m,n))).
// =============================================================
public class Lesson197_MedianOfTwoSortedArrays{
  static double findMedianSortedArrays(int[] a,int[] b){if(a.length>b.length){int[] t=a;a=b;b=t;}int m=a.length,n=b.length,lo=0,hi=m;while(lo<=hi){int i=(lo+hi)/2;int j=(m+n+1)/2-i;int Lx=i>0?a[i-1]:Integer.MIN_VALUE;int Rx=i<m?a[i]:Integer.MAX_VALUE;int Ly=j>0?b[j-1]:Integer.MIN_VALUE;int Ry=j<n?b[j]:Integer.MAX_VALUE;if(Lx<=Ry&&Ly<=Rx){if(((m+n)&1)==1)return Math.max(Lx,Ly);return (Math.max(Lx,Ly)+Math.min(Rx,Ry))/2.0;}else if(Lx>Ry)hi=i-1;else lo=i+1;}return 0;}
  public static void main(String[]a){System.out.println(findMedianSortedArrays(new int[]{1,3},new int[]{2}));System.out.println(findMedianSortedArrays(new int[]{1,2},new int[]{3,4}));}
}
