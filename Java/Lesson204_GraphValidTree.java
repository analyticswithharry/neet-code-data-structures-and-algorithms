// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 204 -- Graph Valid Tree
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 102
// =============================================================
//
// QUESTION:
//   Given n nodes and edges, determine if they form a tree (connected and no cycles).
// =============================================================
public class Lesson204_GraphValidTree{
  static int[] P; static int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
  static boolean validTree(int n,int[][] e){if(e.length!=n-1)return false;P=new int[n];for(int i=0;i<n;i++)P[i]=i;for(int[] x:e){int ra=find(x[0]),rb=find(x[1]);if(ra==rb)return false;P[ra]=rb;}return true;}
  public static void main(String[]a){System.out.println(validTree(5,new int[][]{{0,1},{0,2},{0,3},{1,4}}));System.out.println(validTree(5,new int[][]{{0,1},{1,2},{2,3},{1,3},{1,4}}));}
}
