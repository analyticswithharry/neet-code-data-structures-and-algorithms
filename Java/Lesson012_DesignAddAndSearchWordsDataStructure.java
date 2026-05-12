// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 012 -- Design Add And Search Words Data Structure
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Design a data structure that supports:
//     addWord(word)
//     search(word)  - word may contain '.' which matches any single letter
//
//   Example:
//     d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
//     d.search("pad") -> False
//     d.search("bad") -> True
//     d.search(".ad") -> True
//     d.search("b..") -> True
// =============================================================

import java.util.*;

public class Lesson012_DesignAddAndSearchWordsDataStructure {
    static class WordDictionary {
        Map<Character, WordDictionary> ch = new HashMap<>(); boolean end;
        public void addWord(String w) {
            WordDictionary n = this;
            for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new WordDictionary());
            n.end = true;
        }
        public boolean search(String w) { return dfs(0, w, this); }
        boolean dfs(int i, String w, WordDictionary n) {
            if (i == w.length()) return n.end;
            char c = w.charAt(i);
            if (c == '.') {
                for (WordDictionary x : n.ch.values()) if (dfs(i+1, w, x)) return true;
                return false;
            }
            WordDictionary nx = n.ch.get(c);
            return nx != null && dfs(i+1, w, nx);
        }
    }
    public static void main(String[] args) {
        WordDictionary d = new WordDictionary();
        for (String w : new String[]{"bad","dad","mad"}) d.addWord(w);
        System.out.println(d.search("pad") + " " + d.search("bad") + " " + d.search(".ad") + " " + d.search("b.."));
    }
}
