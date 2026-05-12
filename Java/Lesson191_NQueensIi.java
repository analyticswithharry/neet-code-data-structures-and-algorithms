// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 191 -- N Queens II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return number of distinct solutions for n-queens.
// =============================================================
import java.util.*;
public class Lesson191_NQueensIi{
  static int CNT; static int N; static Set<Integer> C,D1,D2;
  static void bt(int r){if(r==N){CNT++;return;}for(int i=0;i<N;i++){if(C.contains(i)||D1.contains(r-i)||D2.contains(r+i))continue;C.add(i);D1.add(r-i);D2.add(r+i);bt(r+1);C.remove(i);D1.remove(r-i);D2.remove(r+i);}}
  static int totalNQueens(int n){CNT=0;N=n;C=new HashSet<>();D1=new HashSet<>();D2=new HashSet<>();bt(0);return CNT;}
  public static void main(String[]a){System.out.println(totalNQueens(4));System.out.println(totalNQueens(8));}
}
