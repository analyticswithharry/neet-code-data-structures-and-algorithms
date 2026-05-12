// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 023 -- Extra Characters in a String
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given a string s and a dictionary of words, break s into one or more
//   non-overlapping substrings such that each substring is in dictionary.
//   There may be characters in s that are not in any of the substrings.
//   Return the minimum number of extra characters left over.
//
//   Example:
//     Input : s = "leetscode", dict = ["leet","code","leetcode"]
//     Output: 1   (the 's' is extra)
// =============================================================

import java.util.*;
public class Lesson023_ExtraCharactersInAString {
    public int minExtraChar(String s, String[] dictionary) {
        Set<String> words = new HashSet<>(Arrays.asList(dictionary));
        int n = s.length(); int[] dp = new int[n+1];
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1] + 1;
            for (int j = 0; j < i; j++)
                if (words.contains(s.substring(j,i))) dp[i] = Math.min(dp[i], dp[j]);
        }
        return dp[n];
    }
    public static void main(String[] args) {
        System.out.println(new Lesson023_ExtraCharactersInAString().minExtraChar("leetscode", new String[]{"leet","code","leetcode"}));
    }
}
