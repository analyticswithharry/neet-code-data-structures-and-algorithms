// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 024 -- Word Search II
// Category   : Tries
// Difficulty : Hard
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given an m x n board of characters and a list of strings words, return
//   all words on the board. Each word must be constructed from letters of
//   sequentially adjacent cells (horizontal/vertical). The same cell may not
//   be used more than once in a word.
//
//   Example:
//     board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
//     words=["oath","pea","eat","rain"]
//     Output: ["oath","eat"]
// =============================================================

import java.util.*;
public class Lesson024_WordSearchIi {
    static class Node { Map<Character,Node> ch = new HashMap<>(); String word; }
    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) { Node n = root; for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new Node()); n.word = w; }
        Set<String> out = new HashSet<>();
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, out);
        return new ArrayList<>(out);
    }
    void dfs(char[][] b, int r, int c, Node n, Set<String> out) {
        char ch = b[r][c];
        Node nxt = n.ch.get(ch); if (nxt == null) return;
        if (nxt.word != null) out.add(nxt.word);
        b[r][c] = '*';
        int[][] D = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int[] d : D) {
            int nr=r+d[0], nc=c+d[1];
            if (nr>=0&&nr<b.length&&nc>=0&&nc<b[0].length&&b[nr][nc]!='*') dfs(b,nr,nc,nxt,out);
        }
        b[r][c] = ch;
    }
    public static void main(String[] args) {
        char[][] b = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        List<String> r = new Lesson024_WordSearchIi().findWords(b, new String[]{"oath","pea","eat","rain"});
        Collections.sort(r); System.out.println(r);
    }
}
