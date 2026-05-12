// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 180 -- House Robber III
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.
// =============================================================
public class Lesson180_HouseRobberIii{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int[] rec(N n){if(n==null)return new int[]{0,0};int[] l=rec(n.l),r=rec(n.r);return new int[]{n.v+l[1]+r[1],Math.max(l[0],l[1])+Math.max(r[0],r[1])};}
  static int rob(N r){int[] x=rec(r);return Math.max(x[0],x[1]);}
  public static void main(String[]a){N r=new N(3);r.l=new N(2);r.l.r=new N(3);r.r=new N(3);r.r.r=new N(1);System.out.println(rob(r));}
}
