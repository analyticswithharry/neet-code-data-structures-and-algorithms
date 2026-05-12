// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 173 -- Pacific Atlantic Water Flow
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).
// =============================================================
import java.util.*;
public class Lesson173_PacificAtlanticWaterFlow{
  static int R,C; static int[][] H; static int[][] DIR={{1,0},{-1,0},{0,1},{0,-1}};
  static void dfs(int r,int c,boolean[][] s){s[r][c]=true;for(int[] d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&!s[nr][nc]&&H[nr][nc]>=H[r][c])dfs(nr,nc,s);}}
  static List<int[]> pacificAtlantic(int[][] h){R=h.length;C=h[0].length;H=h;boolean[][] pac=new boolean[R][C],atl=new boolean[R][C];for(int c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(int r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}List<int[]> res=new ArrayList<>();for(int r=0;r<R;r++)for(int c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.add(new int[]{r,c});return res;}
  public static void main(String[]a){System.out.println(pacificAtlantic(new int[][]{{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}).size());}
}
