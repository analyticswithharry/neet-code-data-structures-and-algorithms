// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 205 -- Course Schedule IV
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?
// =============================================================
import java.util.*;
public class Lesson205_CourseScheduleIv{
  static List<Boolean> checkIfPrerequisite(int n,int[][] pre,int[][] qs){boolean[][] r=new boolean[n][n];List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[0]).add(p[1]);ind[p[1]]++;r[p[0]][p[1]]=true;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);List<Integer> order=new ArrayList<>();while(!q.isEmpty()){int x=q.poll();order.add(x);for(int y:g.get(x))if(--ind[y]==0)q.add(y);}for(int x:order)for(int y:g.get(x))for(int k=0;k<n;k++)if(r[k][x])r[k][y]=true;List<Boolean> out=new ArrayList<>();for(int[] qq:qs)out.add(r[qq[0]][qq[1]]);return out;}
  public static void main(String[]a){System.out.println(checkIfPrerequisite(3,new int[][]{{1,2},{1,0},{2,0}},new int[][]{{1,0},{1,2}}));}
}
