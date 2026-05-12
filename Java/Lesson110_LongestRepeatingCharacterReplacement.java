// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 110 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 55
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.
// =============================================================

public class Lesson110_LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k){
        int[] cnt = new int[26]; int l=0, mx=0, best=0;
        for (int r=0;r<s.length();r++){
            cnt[s.charAt(r)-'A']++; mx = Math.max(mx, cnt[s.charAt(r)-'A']);
            if (r-l+1 - mx > k){ cnt[s.charAt(l)-'A']--; l++; }
            best = Math.max(best, r-l+1);
        }
        return best;
    }
    public static void main(String[] a){
        Lesson110_LongestRepeatingCharacterReplacement x = new Lesson110_LongestRepeatingCharacterReplacement();
        System.out.println(x.characterReplacement("ABAB", 2));
        System.out.println(x.characterReplacement("AABABBA", 1));
    }
}
