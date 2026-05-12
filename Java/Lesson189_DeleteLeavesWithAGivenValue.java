// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 189 -- Delete Leaves With a Given Value
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Delete all leaf nodes with a given target value (cascade).
// =============================================================
public class Lesson189_DeleteLeavesWithAGivenValue{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static N rem(N n,int t){if(n==null)return null;n.l=rem(n.l,t);n.r=rem(n.r,t);if(n.l==null&&n.r==null&&n.v==t)return null;return n;}
  static String show(N n){if(n==null)return "null";return "["+n.v+","+show(n.l)+","+show(n.r)+"]";}
  public static void main(String[]a){N r=new N(1);r.l=new N(2);r.l.l=new N(2);r.r=new N(3);r.r.l=new N(2);r.r.r=new N(4);System.out.println(show(rem(r,2)));}
}
