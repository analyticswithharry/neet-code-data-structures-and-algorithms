// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 047 -- Longest Repeating Character Replacement
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 23
// =============================================================
//
// QUESTION:
//   Given a string s and integer k, you can change at most k characters.
//   Return length of the longest substring with all same characters.
//
//   Example: s="AABABBA", k=1 -> 4
// =============================================================

public class Lesson047_LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k) {
        int[] cnt = new int[26]; int l=0, best=0, mf=0;
        for (int r=0;r<s.length();r++) {
            cnt[s.charAt(r)-'A']++;
            mf = Math.max(mf, cnt[s.charAt(r)-'A']);
            if (r - l + 1 - mf > k) { cnt[s.charAt(l)-'A']--; l++; }
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new Lesson047_LongestRepeatingCharacterReplacement().characterReplacement("AABABBA", 1));
    }
}
