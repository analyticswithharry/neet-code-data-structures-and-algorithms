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

var checkInclusion = function(s1, s2) {
    if (s1.length > s2.length) return false;
    const a = new Array(26).fill(0), b = new Array(26).fill(0);
    for (const c of s1) a[c.charCodeAt(0)-97]++;
    for (let i=0;i<s1.length;i++) b[s2.charCodeAt(i)-97]++;
    const eq = () => a.every((v,i)=>v===b[i]);
    if (eq()) return true;
    for (let i=s1.length;i<s2.length;i++) {
        b[s2.charCodeAt(i)-97]++;
        b[s2.charCodeAt(i-s1.length)-97]--;
        if (eq()) return true;
    }
    return false;
};
console.log(checkInclusion("ab","eidbaooo"), checkInclusion("ab","eidboaoo"));
