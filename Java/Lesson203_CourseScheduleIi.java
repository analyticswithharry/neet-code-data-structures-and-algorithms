// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 203 -- Course Schedule II
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Return any topological ordering of courses, or empty array if impossible.
// =============================================================
import java.util.*;
public class Lesson203_CourseScheduleIi{
  static int[] findOrder(int n,int[][] pre){List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[1]).add(p[0]);ind[p[0]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);int[] res=new int[n];int k=0;while(!q.isEmpty()){int x=q.poll();res[k++]=x;for(int y:g.get(x))if(--ind[y]==0)q.add(y);}return k==n?res:new int[0];}
  public static void main(String[]a){System.out.println(Arrays.toString(findOrder(4,new int[][]{{1,0},{2,0},{3,1},{3,2}})));}
}
