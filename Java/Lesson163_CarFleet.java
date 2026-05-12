// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 163 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
// =============================================================
import java.util.*;
public class Lesson163_CarFleet{
  static int carFleet(int target,int[] pos,int[] sp){int n=pos.length;Integer[] idx=new Integer[n];for(int i=0;i<n;i++)idx[i]=i;Arrays.sort(idx,(a,b)->pos[b]-pos[a]);int f=0;double lt=0;for(int i:idx){double t=(double)(target-pos[i])/sp[i];if(t>lt){f++;lt=t;}}return f;}
  public static void main(String[]a){System.out.println(carFleet(12,new int[]{10,8,0,5,3},new int[]{2,4,1,1,3}));}
}
