// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 176 -- Kth Smallest Element In a Bst
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 88
// =============================================================
//
// QUESTION:
//   Return the kth smallest value in a BST (1-indexed).
// =============================================================
import java.util.*;
public class Lesson176_KthSmallestElementInABst{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int kth(N r,int k){Deque<N> st=new ArrayDeque<>();N cur=r;while(cur!=null||!st.isEmpty()){while(cur!=null){st.push(cur);cur=cur.l;}cur=st.pop();if(--k==0)return cur.v;cur=cur.r;}return -1;}
  public static void main(String[]a){N r=new N(3);r.l=new N(1);r.l.r=new N(2);r.r=new N(4);System.out.println(kth(r,1));System.out.println(kth(r,3));}
}
