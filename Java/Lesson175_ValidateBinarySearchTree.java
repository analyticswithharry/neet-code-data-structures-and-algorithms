// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 175 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Determine if a binary tree is a valid BST.
// =============================================================
public class Lesson175_ValidateBinarySearchTree{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static boolean rec(N n,long lo,long hi){if(n==null)return true;if(n.v<=lo||n.v>=hi)return false;return rec(n.l,lo,n.v)&&rec(n.r,n.v,hi);}
  static boolean isValidBST(N r){return rec(r,Long.MIN_VALUE,Long.MAX_VALUE);}
  public static void main(String[]a){N r=new N(2);r.l=new N(1);r.r=new N(3);System.out.println(isValidBST(r));}
}
