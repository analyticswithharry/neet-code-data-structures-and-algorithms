// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 199 -- Stone Game II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 100
// =============================================================
//
// QUESTION:
//   Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.
// =============================================================
import java.util.*;
public class Lesson199_StoneGameIi{
  static int[] SUF; static int N; static int[][] M;
  static int dfs(int i,int m){if(i+2*m>=N)return SUF[i];if(M[i][m]!=-1)return M[i][m];int best=0;for(int x=1;x<=2*m;x++)best=Math.max(best,SUF[i]-dfs(i+x,Math.max(m,x)));return M[i][m]=best;}
  static int stoneGameII(int[] p){N=p.length;SUF=new int[N+1];for(int i=N-1;i>=0;i--)SUF[i]=SUF[i+1]+p[i];M=new int[N+1][N+1];for(int[] r:M)Arrays.fill(r,-1);return dfs(0,1);}
  public static void main(String[]a){System.out.println(stoneGameII(new int[]{2,7,9,4,4}));}
}
