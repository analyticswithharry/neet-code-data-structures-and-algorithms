// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 186 -- Gas Station
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).
// =============================================================
public class Lesson186_GasStation{
  static int canCompleteCircuit(int[] g,int[] c){int s=0,t=0,tot=0;for(int i=0;i<g.length;i++){int d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
  public static void main(String[]a){System.out.println(canCompleteCircuit(new int[]{1,2,3,4,5},new int[]{3,4,5,1,2}));System.out.println(canCompleteCircuit(new int[]{2,3,4},new int[]{3,4,3}));}
}
