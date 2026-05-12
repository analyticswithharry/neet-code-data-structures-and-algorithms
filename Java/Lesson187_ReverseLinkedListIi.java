// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 187 -- Reverse Linked List II
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Reverse the nodes of the list from position left to right (1-indexed).
// =============================================================
import java.util.*;
public class Lesson187_ReverseLinkedListIi{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N reverseBetween(N h,int L,int R){N d=new N(0);d.n=h;N pre=d;for(int i=0;i<L-1;i++)pre=pre.n;N cur=pre.n;for(int i=0;i<R-L;i++){N nxt=cur.n;cur.n=nxt.n;nxt.n=pre.n;pre.n=nxt;}return d.n;}
  public static void main(String[]a){N h=new N(1);N c=h;for(int v:new int[]{2,3,4,5}){c.n=new N(v);c=c.n;}N r=reverseBetween(h,2,4);List<Integer> out=new ArrayList<>();while(r!=null){out.add(r.v);r=r.n;}System.out.println(out);}
}
