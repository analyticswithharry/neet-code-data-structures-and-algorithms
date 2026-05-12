// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 170 -- Target Sum
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 85
// =============================================================
//
// QUESTION:
//   Assign + or - to each number so the sum equals target. Return number of ways.
// =============================================================
import java.util.*;
public class Lesson170_TargetSum{
  static int findTargetSumWays(int[] nums,int target){Map<Integer,Integer> dp=new HashMap<>();dp.put(0,1);for(int n:nums){Map<Integer,Integer> nd=new HashMap<>();for(var e:dp.entrySet()){nd.merge(e.getKey()+n,e.getValue(),Integer::sum);nd.merge(e.getKey()-n,e.getValue(),Integer::sum);}dp=nd;}return dp.getOrDefault(target,0);}
  public static void main(String[]a){System.out.println(findTargetSumWays(new int[]{1,1,1,1,1},3));}
}
