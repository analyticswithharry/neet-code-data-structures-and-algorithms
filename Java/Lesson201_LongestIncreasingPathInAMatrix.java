// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 201 -- Longest Increasing Path In a Matrix
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 101
// =============================================================
//
// QUESTION:
//   Find length of the longest strictly-increasing path in a 2D grid.
// =============================================================
public class Lesson201_LongestIncreasingPathInAMatrix{
  static int R,C; static int[][] G,M; static int[][] DIR={{1,0},{-1,0},{0,1},{0,-1}};
  static int dfs(int r,int c){if(M[r][c]!=0)return M[r][c];int best=1;for(int[] d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c])best=Math.max(best,1+dfs(nr,nc));}return M[r][c]=best;}
  static int longestIncreasingPath(int[][] g){R=g.length;C=g[0].length;G=g;M=new int[R][C];int res=0;for(int r=0;r<R;r++)for(int c=0;c<C;c++)res=Math.max(res,dfs(r,c));return res;}
  public static void main(String[]a){System.out.println(longestIncreasingPath(new int[][]{{9,9,4},{6,6,8},{2,1,1}}));}
}
