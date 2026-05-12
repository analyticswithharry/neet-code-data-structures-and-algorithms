// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 011 -- Implement Trie Prefix Tree
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Implement the Trie class with:
//     insert(word)        - inserts the word
//     search(word)        - returns true if word is in trie
//     startsWith(prefix)  - returns true if any word starts with prefix
//
//   Example:
//     trie = Trie()
//     trie.insert("apple")
//     trie.search("apple")   -> True
//     trie.search("app")     -> False
//     trie.startsWith("app") -> True
//     trie.insert("app")
//     trie.search("app")     -> True
// =============================================================

import java.util.*;

public class Lesson011_ImplementTriePrefixTree {
    static class Trie {
        Map<Character, Trie> ch = new HashMap<>();
        boolean end;
        public void insert(String w) {
            Trie n = this;
            for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new Trie());
            n.end = true;
        }
        Trie walk(String w) {
            Trie n = this;
            for (char c : w.toCharArray()) { n = n.ch.get(c); if (n == null) return null; }
            return n;
        }
        public boolean search(String w) { Trie n = walk(w); return n != null && n.end; }
        public boolean startsWith(String p) { return walk(p) != null; }
    }
    public static void main(String[] args) {
        Trie t = new Trie(); t.insert("apple");
        System.out.println(t.search("apple") + " " + t.search("app") + " " + t.startsWith("app"));
        t.insert("app"); System.out.println(t.search("app"));
    }
}
