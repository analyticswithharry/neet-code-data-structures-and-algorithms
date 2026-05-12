// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 092 -- Reorganize String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.
// =============================================================

import java.util.*;
public class Lesson092_ReorganizeString {
    public String reorganizeString(String s){
        int[] c = new int[26];
        for (char ch: s.toCharArray()) c[ch-'a']++;
        int n=s.length(), mx=0, idx=0;
        for (int i=0;i<26;i++) if (c[i]>mx){ mx=c[i]; idx=i; }
        if (mx > (n+1)/2) return "";
        char[] res = new char[n]; int i=0;
        while (c[idx]>0){ res[i]=(char)('a'+idx); i+=2; c[idx]--; }
        for (int k=0;k<26;k++){
            while (c[k]>0){ if (i>=n) i=1; res[i]=(char)('a'+k); i+=2; c[k]--; }
        }
        return new String(res);
    }
    public static void main(String[] a){
        System.out.println(new Lesson092_ReorganizeString().reorganizeString("aab"));
        System.out.println("[" + new Lesson092_ReorganizeString().reorganizeString("aaab") + "]");
    }
}
