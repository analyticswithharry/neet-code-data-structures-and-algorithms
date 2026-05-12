// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 161 -- Pow x n
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Implement pow(x, n) — x raised to the n-th power.
// =============================================================
public class Lesson161_PowXN{
  static double myPow(double x,long n){if(n<0){x=1/x;n=-n;}double r=1.0;while(n>0){if((n&1)==1)r*=x;x*=x;n>>=1;}return r;}
  public static void main(String[]a){System.out.println(myPow(2.0,10));System.out.println(myPow(2.0,-2));}
}
