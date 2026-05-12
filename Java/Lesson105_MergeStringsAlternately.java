// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 105 -- Merge Strings Alternately
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 53
// =============================================================
//
// QUESTION:
//   Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.
// =============================================================

public class Lesson105_MergeStringsAlternately {
    public String mergeAlternately(String a, String b){
        StringBuilder sb = new StringBuilder(); int i=0;
        while (i<a.length() || i<b.length()){
            if (i<a.length()) sb.append(a.charAt(i));
            if (i<b.length()) sb.append(b.charAt(i));
            i++;
        }
        return sb.toString();
    }
    public static void main(String[] a){
        Lesson105_MergeStringsAlternately x = new Lesson105_MergeStringsAlternately();
        System.out.println(x.mergeAlternately("abc","pqr"));
        System.out.println(x.mergeAlternately("ab","pqrs"));
    }
}
