// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 036 -- Valid Anagram
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 18
// =============================================================
//
// QUESTION:
//   Given two strings s and t, return true if t is an anagram of s.
//
//   Example: s = "anagram", t = "nagaram" -> true
// =============================================================

import java.util.*;
public class Lesson036_ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()) return false;
        int[] c = new int[26];
        for (int i=0;i<s.length();i++){ c[s.charAt(i)-'a']++; c[t.charAt(i)-'a']--; }
        for (int x: c) if (x!=0) return false;
        return true;
    }
    public static void main(String[] a){
        Lesson036_ValidAnagram s = new Lesson036_ValidAnagram();
        System.out.println(s.isAnagram("anagram","nagaram"));
        System.out.println(s.isAnagram("rat","car"));
    }
}
