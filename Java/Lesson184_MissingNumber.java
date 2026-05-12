// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 184 -- Missing Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 92
// =============================================================
//
// QUESTION:
//   Array contains n distinct numbers from [0,n]. Return the missing one.
// =============================================================
public class Lesson184_MissingNumber{
  static int missing(int[] a){int x=a.length;for(int i=0;i<a.length;i++)x^=i^a[i];return x;}
  public static void main(String[]a){System.out.println(missing(new int[]{3,0,1}));System.out.println(missing(new int[]{9,6,4,2,3,5,7,0,1}));}
}
