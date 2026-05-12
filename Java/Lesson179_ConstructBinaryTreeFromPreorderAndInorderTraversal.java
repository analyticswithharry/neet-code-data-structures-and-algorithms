// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 179 -- Construct Binary Tree From Preorder And Inorder Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 90
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.
// =============================================================
import java.util.*;
public class Lesson179_ConstructBinaryTreeFromPreorderAndInorderTraversal{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int p; static int[] PRE; static Map<Integer,Integer> IDX;
  static N rec(int lo,int hi){if(lo>hi)return null;int v=PRE[p++];int k=IDX.get(v);N n=new N(v);n.l=rec(lo,k-1);n.r=rec(k+1,hi);return n;}
  static N build(int[] pre,int[] ino){p=0;PRE=pre;IDX=new HashMap<>();for(int i=0;i<ino.length;i++)IDX.put(ino[i],i);return rec(0,ino.length-1);}
  static List<Integer> pre_order(N n){List<Integer> r=new ArrayList<>();if(n==null)return r;r.add(n.v);r.addAll(pre_order(n.l));r.addAll(pre_order(n.r));return r;}
  public static void main(String[]a){System.out.println(pre_order(build(new int[]{3,9,20,15,7},new int[]{9,3,15,20,7})));}
}
