// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 048 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 24
// =============================================================
//
// QUESTION:
//   Given s1 and s2, return true if s2 contains a permutation of s1.
//
//   Example: s1="ab", s2="eidbaooo" -> true
// =============================================================

import java.util.*;
public class Lesson048_PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length()) return false;
        int[] a = new int[26], b = new int[26];
        for (int i=0;i<s1.length();i++) { a[s1.charAt(i)-'a']++; b[s2.charAt(i)-'a']++; }
        if (Arrays.equals(a,b)) return true;
        for (int i=s1.length();i<s2.length();i++) {
            b[s2.charAt(i)-'a']++;
            b[s2.charAt(i-s1.length())-'a']--;
            if (Arrays.equals(a,b)) return true;
        }
        return false;
    }
    public static void main(String[] x){
        Lesson048_PermutationInString s = new Lesson048_PermutationInString();
        System.out.println(s.checkInclusion("ab","eidbaooo"));
        System.out.println(s.checkInclusion("ab","eidboaoo"));
    }
}
