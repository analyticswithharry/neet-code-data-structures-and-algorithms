// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 190 -- Binary Tree Maximum Path Sum
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 95
// =============================================================
//
// QUESTION:
//   Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.
// =============================================================
public class Lesson190_BinaryTreeMaximumPathSum{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int res; static int dfs(N n){if(n==null)return 0;int l=Math.max(0,dfs(n.l)),r=Math.max(0,dfs(n.r));res=Math.max(res,n.v+l+r);return n.v+Math.max(l,r);}
  static int maxPathSum(N r){res=Integer.MIN_VALUE;dfs(r);return res;}
  public static void main(String[]a){N r=new N(-10);r.l=new N(9);r.r=new N(20);r.r.l=new N(15);r.r.r=new N(7);System.out.println(maxPathSum(r));}
}
