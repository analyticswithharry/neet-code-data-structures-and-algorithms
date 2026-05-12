// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 046 -- Longest Substring Without Repeating Characters
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string, find the length of the longest substring without
//   repeating characters.
//
//   Example: "abcabcbb" -> 3
// =============================================================

import java.util.*;
public class Lesson046_LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> seen = new HashMap<>();
        int l=0, best=0;
        for (int r=0;r<s.length();r++) {
            char c = s.charAt(r);
            if (seen.containsKey(c) && seen.get(c) >= l) l = seen.get(c)+1;
            seen.put(c, r);
            best = Math.max(best, r-l+1);
        }
        return best;
    }
    public static void main(String[] a){
        Lesson046_LongestSubstringWithoutRepeatingCharacters s = new Lesson046_LongestSubstringWithoutRepeatingCharacters();
        System.out.println(s.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(s.lengthOfLongestSubstring("bbbbb"));
    }
}
