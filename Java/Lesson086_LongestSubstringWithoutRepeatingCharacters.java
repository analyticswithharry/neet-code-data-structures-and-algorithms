// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 086 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given a string s, find the length of the longest substring without repeating characters.
//   Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.
// =============================================================

import java.util.*;
public class Lesson086_LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s){
        Map<Character,Integer> m = new HashMap<>();
        int l=0, best=0;
        for (int r=0;r<s.length();r++){
            char c=s.charAt(r);
            if (m.containsKey(c) && m.get(c)>=l) l = m.get(c)+1;
            m.put(c,r); best = Math.max(best, r-l+1);
        } return best;
    }
    public static void main(String[] a){
        Lesson086_LongestSubstringWithoutRepeatingCharacters x = new Lesson086_LongestSubstringWithoutRepeatingCharacters();
        System.out.println(x.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(x.lengthOfLongestSubstring("pwwkew"));
    }
}
