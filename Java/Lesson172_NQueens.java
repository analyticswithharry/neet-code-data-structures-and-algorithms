// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 172 -- N Queens
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Place n queens on n×n board so none attack each other; return the count of distinct solutions.
// =============================================================
import java.util.*;
public class Lesson172_NQueens{
  static int cnt; static int N; static Set<Integer> cols,d1,d2;
  static void bt(int r){if(r==N){cnt++;return;}for(int c=0;c<N;c++){if(cols.contains(c)||d1.contains(r-c)||d2.contains(r+c))continue;cols.add(c);d1.add(r-c);d2.add(r+c);bt(r+1);cols.remove(c);d1.remove(r-c);d2.remove(r+c);}}
  static int totalNQueens(int n){cnt=0;N=n;cols=new HashSet<>();d1=new HashSet<>();d2=new HashSet<>();bt(0);return cnt;}
  public static void main(String[]a){System.out.println(totalNQueens(4));System.out.println(totalNQueens(6));}
}
