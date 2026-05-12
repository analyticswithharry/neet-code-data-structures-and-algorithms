// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 206 -- Number of Connected Components In An Undirected Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 103
// =============================================================
//
// QUESTION:
//   Given n nodes and undirected edges, return the number of connected components.
// =============================================================
public class Lesson206_NumberOfConnectedComponentsInAnUndirectedGraph{
  static int[] P; static int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
  static int countComponents(int n,int[][] e){P=new int[n];for(int i=0;i<n;i++)P[i]=i;int cnt=n;for(int[] x:e){int ra=find(x[0]),rb=find(x[1]);if(ra!=rb){P[ra]=rb;cnt--;}}return cnt;}
  public static void main(String[]a){System.out.println(countComponents(5,new int[][]{{0,1},{1,2},{3,4}}));}
}
