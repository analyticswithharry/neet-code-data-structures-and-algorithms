// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 100 -- Palindrome Partitioning
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Partition string s such that every substring is a palindrome. Return all possible partitions.
// =============================================================

import java.util.*;
public class Lesson100_PalindromePartitioning {
    List<List<String>> res = new ArrayList<>();
    boolean isPal(String s){ for (int i=0,j=s.length()-1;i<j;i++,j--) if (s.charAt(i)!=s.charAt(j)) return false; return true; }
    void bt(String s, int i, List<String> cur){
        if (i==s.length()){ res.add(new ArrayList<>(cur)); return; }
        for (int j=i+1;j<=s.length();j++){
            String sub = s.substring(i,j);
            if (isPal(sub)){ cur.add(sub); bt(s,j,cur); cur.remove(cur.size()-1); }
        }
    }
    public List<List<String>> partition(String s){ bt(s,0,new ArrayList<>()); return res; }
    public static void main(String[] a){ System.out.println(new Lesson100_PalindromePartitioning().partition("aab")); }
}
