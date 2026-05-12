// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 182 -- Course Schedule
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   Given prerequisites pairs, can all courses be finished (no cycle)?
// =============================================================
import java.util.*;
public class Lesson182_CourseSchedule{
  static boolean canFinish(int n,int[][] pre){List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[1]).add(p[0]);ind[p[0]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);int cnt=0;while(!q.isEmpty()){int x=q.poll();cnt++;for(int y:g.get(x))if(--ind[y]==0)q.add(y);}return cnt==n;}
  public static void main(String[]a){System.out.println(canFinish(2,new int[][]{{1,0}}));System.out.println(canFinish(2,new int[][]{{1,0},{0,1}}));}
}
