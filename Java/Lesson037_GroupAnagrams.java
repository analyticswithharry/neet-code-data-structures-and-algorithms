// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 037 -- Group Anagrams
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given an array of strings strs, group the anagrams together.
//
//   Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
// =============================================================

import java.util.*;
public class Lesson037_GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> m = new HashMap<>();
        for (String s: strs) {
            char[] a = s.toCharArray(); Arrays.sort(a);
            String k = new String(a);
            m.computeIfAbsent(k, x -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(m.values());
    }
    public static void main(String[] a){
        System.out.println(new Lesson037_GroupAnagrams().groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
    }
}
