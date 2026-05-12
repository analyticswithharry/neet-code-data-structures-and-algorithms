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

var minExtraChar = function(s, dictionary) {
    const words = new Set(dictionary), n = s.length;
    const dp = new Array(n+1).fill(0);
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i-1] + 1;
        for (let j = 0; j < i; j++) if (words.has(s.slice(j,i))) dp[i] = Math.min(dp[i], dp[j]);
    }
    return dp[n];
};
console.log(minExtraChar("leetscode", ["leet","code","leetcode"]));
