// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 028 -- Verifying An Alien Dictionary
// Category   : Graphs
// Difficulty : Easy
// Study Plan : Day 14
// =============================================================
//
// QUESTION:
//   In an alien language, surprisingly, they also use English lowercase
//   letters but possibly in a different order. Given a sequence of words
//   written in the alien language and the order of the alphabet, return true
//   iff the given words are sorted lexicographically in this alien language.
//
//   Example:
//     Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
//     Output: true
// =============================================================

public class Lesson028_VerifyingAnAlienDictionary {
    public boolean isAlienSorted(String[] words, String order) {
        int[] idx = new int[26];
        for (int i = 0; i < 26; i++) idx[order.charAt(i)-'a'] = i;
        for (int w = 1; w < words.length; w++) {
            String a = words[w-1], b = words[w]; boolean broke = false;
            int n = Math.min(a.length(), b.length());
            for (int i = 0; i < n; i++) {
                int ia = idx[a.charAt(i)-'a'], ib = idx[b.charAt(i)-'a'];
                if (ia != ib) { if (ia > ib) return false; broke = true; break; }
            }
            if (!broke && a.length() > b.length()) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(new Lesson028_VerifyingAnAlienDictionary().isAlienSorted(new String[]{"hello","leetcode"}, "hlabcdefgijkmnopqrstuvwxyz"));
    }
}
