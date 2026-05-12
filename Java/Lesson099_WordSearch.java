// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 099 -- Word Search
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Given an m x n board and a word, return true if the word exists by sequentially adjacent cells (no reuse).
// =============================================================

public class Lesson099_WordSearch {
    char[][] b; String w;
    boolean dfs(int r,int c,int i){
        if (i==w.length()) return true;
        if (r<0||r>=b.length||c<0||c>=b[0].length||b[r][c]!=w.charAt(i)) return false;
        char t=b[r][c]; b[r][c]='#';
        boolean ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
        b[r][c]=t; return ok;
    }
    public boolean exist(char[][] board, String word){
        b=board; w=word;
        for (int r=0;r<b.length;r++) for (int c=0;c<b[0].length;c++) if (dfs(r,c,0)) return true;
        return false;
    }
    public static void main(String[] a){
        char[][] bd={{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        System.out.println(new Lesson099_WordSearch().exist(bd, "ABCCED"));
    }
}
