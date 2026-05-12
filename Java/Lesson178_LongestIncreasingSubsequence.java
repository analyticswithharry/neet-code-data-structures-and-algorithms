// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 178 -- Longest Increasing Subsequence
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Length of the longest strictly-increasing subsequence.
// =============================================================
import java.util.*;
public class Lesson178_LongestIncreasingSubsequence{
  static int LIS(int[] a){List<Integer> t=new ArrayList<>();for(int x:a){int lo=0,hi=t.size();while(lo<hi){int m=(lo+hi)>>>1;if(t.get(m)<x)lo=m+1;else hi=m;}if(lo==t.size())t.add(x);else t.set(lo,x);}return t.size();}
  public static void main(String[]a){System.out.println(LIS(new int[]{10,9,2,5,3,7,101,18}));}
}
