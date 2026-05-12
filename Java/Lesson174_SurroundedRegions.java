// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 174 -- Surrounded Regions
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 87
// =============================================================
//
// QUESTION:
//   Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).
// =============================================================
public class Lesson174_SurroundedRegions{
  static int R,C; static char[][] B;
  static void dfs(int r,int c){if(r<0||r>=R||c<0||c>=C||B[r][c]!='O')return;B[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}
  static void solve(char[][] b){R=b.length;C=b[0].length;B=b;for(int r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(int c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(int r=0;r<R;r++)for(int c=0;c<C;c++)b[r][c]=b[r][c]=='S'?'O':'X';}
  public static void main(String[]a){char[][] g={{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};solve(g);for(char[] row:g){for(char x:row)System.out.print(x);System.out.println();}}
}
