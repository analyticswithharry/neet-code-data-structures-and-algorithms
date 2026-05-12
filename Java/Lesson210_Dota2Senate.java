// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 210 -- Dota2 Senate
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.
// =============================================================
import java.util.*;
public class Lesson210_Dota2Senate{
  static String predictPartyVictory(String s){Deque<Integer> R=new ArrayDeque<>(),D=new ArrayDeque<>();int n=s.length();for(int i=0;i<n;i++)(s.charAt(i)=='R'?R:D).add(i);while(!R.isEmpty()&&!D.isEmpty()){int r=R.poll(),d=D.poll();if(r<d)R.add(r+n);else D.add(d+n);}return R.isEmpty()?"Dire":"Radiant";}
  public static void main(String[]a){System.out.println(predictPartyVictory("RD"));System.out.println(predictPartyVictory("RDD"));}
}
